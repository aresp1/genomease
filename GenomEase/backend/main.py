# Import required libraries
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import subprocess
from pathlib import Path

# Set project root as parent of the current file's folder
project_root = Path(__file__).resolve().parent.parent

# Define uploads and results directories
UPLOADS_DIR = project_root / "uploads"
RESULTS_DIR = project_root / "results"

# Create the folders at the project root
for folder in [UPLOADS_DIR, RESULTS_DIR]:
    folder.mkdir(exist_ok=True)

app = FastAPI()  # Create the app


@app.post("/run_fastqc")  # Creates an HTTP POST endpoint
async def run_fastqc(file: UploadFile = File(...)):
    """
    Async function to run FastQC on uploaded FASTQ or FASTQ.GZ files.
    It returns an HTML QC report.
    """
    # Validate file extension
    if not file.filename.endswith((".fastq", ".fastq.gz")):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .fastq or .fastq.gz file.")

    # Save the uploaded FASTQ file to the uploads folder
    upload_path = UPLOADS_DIR / file.filename  # We set the output path
    with open(upload_path, "wb") as f:  # Creates a new file on the computer
        f.write(await file.read())  # Writes the FASTQ data to disk

    # Construct report filename and path
    report_path = RESULTS_DIR / f"{upload_path.stem}_fastqc.html"

    try:
        # Run FastQC and put the results inside the folder
        subprocess.run(["fastqc", str(upload_path), "-o", str(RESULTS_DIR)], check=True)
    except subprocess.CalledProcessError:
        # FastQC failed
        raise HTTPException(status_code=500, detail="FastQC failed.")

    # Check if the report actually exists
    if not report_path.exists():
        raise HTTPException(status_code=500, detail="FastQC report not found.")

    return FileResponse(report_path)  # Return the report to the user
