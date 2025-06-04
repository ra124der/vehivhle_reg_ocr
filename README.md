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
[](https://www.python.org/downloads/release/python-3120/)

When Running installer,Click add python(put tick mark) to path during installing

### 2. Python dependencies

Install required Python packages with:

bash
pip install -r path_to_requirements.txt
path_to reuirements.txt is place holder for path of requirements.txt

### 3. External dependencies
1. Tesseract OCR
   
Download and install Tesseract OCR suitable for your OS:

Windows: Use the latest installer from UB Mannheim builds:https://github.com/UB-Mannheim/tesseract/wiki
Download the latest installer suitable for your system (usually the topmost release).

Linux: Install via package manager:sudo apt-get install tesseract-ocr.

macOS:Use Homebrew:brew install tesseract

After installation, set the environment variable TESSERACT_PATH to the full path of the tesseract executable.

Example (Windows CMD):

set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
This is normally where it is installed.just in case check whether this is the actual path of tesseract.exe
PowerShell:

$env:TESSERACT_PATH = "C:\Program Files\Tesseract-OCR\tesseract.exe"

2. Poppler
Required for converting PDF pages to images.

Download Poppler for your OS:

Windows: https://github.com/oschwartz10612/poppler-windows/releases
Download the zip file (e.g., poppler-24.08.0.zip), extract it, and use the Library\bin folder as your POPLER_PATH.

Linux: Use your package manager: '''bash sudo apt-get install poppler-utils

macOS:brew install poppler

Extract (if applicable), then set the environment variable POPLER_PATH to the folder containing Poppler’s binaries (Library\bin on Windows).
set path to folder in your machine where library\bin

Example (Windows CMD):
set POPLER_PATH=C:\poppler-24.08.0\Library\bin

PowerShell:
$env:POPLER_PATH = "C:\poppler-24.08.0\Library\bin"

### 4. Running the Project

Once dependencies and environment variables are set, run the main script:

bash
python main.py --indir "path_to_root_input_folder"

Replace "path_to_root_input_folder" with your folder containing subfolders of images/PDFs.

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
