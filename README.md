# vehivhle_reg_ocr
Extracting vehicle registraion numbers from images or pdfs using ocr
Setup Instructions

# Vehicle Registration Number Extraction

This project extracts vehicle registration numbers from images and PDFs using OCR technology. It primarily uses **Doctr OCR**, and falls back to **Tesseract OCR** if needed.

---

## Features

- Supports image files (`.jpg`, `.jpeg`, `.png`) and PDF files.
- Uses Doctr OCR first; falls back to Tesseract OCR if Doctr fails.
- Normalizes text and extracts vehicle registration numbers using regex.
- Processes multiple folders containing image/PDF files.

---

## Prerequisites

### 1. Python 3.7+

Make sure Python is installed on your system. You can download it here:  
[https://www.python.org/downloads/release/python-3120/](https://www.python.org/downloads/release/python-3120/)

When Running installer,Click add python(put tick mark) to path during installing

### 2. Python dependencies

Install required Python packages with:

bash
pip install -r path_to_requirements.txt
path_to reuirements.txt is place holder for path of requirements.txt

### 3. External dependencies

Windows:

### 🔧 Setting Up Tesseract and Poppler on Windows

1. **Install Tesseract**:
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to: `C:\Program Files\Tesseract-OCR`

2. **Install Poppler**:
   - Download ZIP from: https://github.com/oschwartz10612/poppler-windows/releases
3. **Add to PATH**:
   - Open "Edit the system environment variables" → Environment Variables.
   - Edit `Path` under *System variables* and add:
     - C:\Program Files\Tesseract-OCR
  After extracting the release 24.08.0 find bin folder ,copy the path and paste in system variables by editing path and adding.
     - `C:\depends_on_machine\Release-24.08.0-0\poppler-24.08.0\Library\bin



4. **Verify**:
   Open Command Prompt and run:
   ```cmd
   tesseract --version
   pdftoppm -v
### 4. Running the Project

Once dependencies and environment variables are set, run the main script:

bash
python path_to_main.py --indir "path_to_root_input_folder"

Replace "path_to_root_input_folder" with your folder containing subfolders of images/PDFs.
make sure cmd 

### 5.Environmental Variable Checks

To verify environment variables:

Windows CMD:
echo %TESSERACT_PATH%
echo %POPLER_PATH%

PowerShell:
echo $env:TESSERACT_PATH
echo $env:POPLER_PATH

### 6.Repo Contents

main.py — Main program to run OCR on folders.

doctr_module.py — Code using Doctr OCR.

pytesseract_module.py — Code using Tesseract OCR.

enb.py — Handles environment variable loading and validation.

requirements.txt — Python dependencies list.

6)Troubleshooting

If you see warnings about invalid paths, verify you have installed Tesseract and Poppler correctly and set the environment variables properly.

For Windows, be sure to open a new terminal window after setting environment variables or set them permanently via System Environment Variables in Windows Settings.
