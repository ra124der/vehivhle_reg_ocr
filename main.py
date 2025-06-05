import argparse
import logging
from doctr_module import extract_text_doctr
from pytesseract_module import extract_text_pytesseract
from enb import pytesseract_path, poppler_path
import os
import re

# Remove default handlers and reconfigure logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

regex_pattern = r'[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{4}'

def normtext(text):
    clean_hs = re.sub(r'[\s\-]', '', text.upper())
    chars = list(clean_hs)
    for i in range(len(chars) - 3):
        if chars[i].isalpha() and chars[i+1].isalpha() and chars[i+2] == 'O' and chars[i+3].isdigit():
            chars[i+2] = '0'
    return ''.join(chars)

def find_reg_no(text):
    normalized = normtext(text)
    match = re.search(regex_pattern, normalized)
    return match.group() if match else None

def fallback_method(path):
    text = extract_text_doctr(path)
    if text:
        reg = find_reg_no(text)
        if reg:
            return reg
    text = extract_text_pytesseract(path, poppler_path, pytesseract_path)
    reg2=find_reg_no(text)
    if reg2:
        return reg2
    return "No registration number detected"

def extract_reg_no_from_folder(root_folder):
    for sub in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, sub)
        if not os.path.isdir(subfolder_path) or sub.startswith('_'):
            continue

        found = None
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                found = fallback_method(file_path)
                if found:
                    break

        logger.info(f"{sub} - {found if found else 'No reg no. found'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", required=True, help="Root directory containing subfolders of images/pdfs")
    args = parser.parse_args()
    extract_reg_no_from_folder(args.indir)




