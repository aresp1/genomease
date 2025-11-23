# GenomEase - FASTQ QC Web Tool
**GenomEase** is a FastAPI tool that allows users to upload FASTQ or FASTQ.GZ sequencing files and automatically execute FastQC to produce quality control reports. It is a bioinformatics pipeline that is easy to run locally and extend in the future. 

## Features

- Upload FASTQ or FASTQ.GZ files
- Automatic execution of FastQC on the uploaded file
- Returns an HTML quality control report
- Error handling when FastQC fails or report is missing 

## Requirements

- Python 3.8+ 
- FastQC 
- Python packages: 
	- `fastapi`
	- `uvicorn`
	- `python-multipart` 

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/genomease.git
cd genomease
```
2. Create a virtual environment (it is not necessary but recommended):
```bash
python -m venv venv
```
3. Install Python dependencies:
```bash
pip install fastapi uvicorn python-multipart
```
4. Make sure FastQC is installed and accessible:
```bash
fastqc --version
```

## Running the Server

1. Go to the folder of the project
2. Start the FastAPI server:
```bash
uvicorn backend.main:app --reload
```
3. Open the browser and go to:
- http://127.0.0.1:8000/docs
4. From there you can upload a FASTQ or FASTQ.GZ file and receive the FastQC report.

## Project Structure
```bash
genomease/
├─ backend/
│  └─ main.py              # FastAPI application
├─ uploads/                # Uploaded FASTQ/FASTQ.GZ files (ignored by git)
├─ results/                # FastQC reports (ignored by git)
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## Future Features

- Add a simple web frontend for uploading files
- Run multi-step pipelines (alignment, variant calling)
- Real-time log streaming during pipeline execution
- Cloud storage support (S3, Azure)
- Add user authentication for workflow history

## License
This project is open source under the MIT License.
