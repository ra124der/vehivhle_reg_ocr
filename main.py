import os
import re
from doctr_module import DoctrOCR
from pytesseract_module import TesseractOCR

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

class RegNoExtractor:
    def __init__(self):
        self.doctr_ocr = DoctrOCR()
        self.tesseract_ocr = TesseractOCR()

    def extract_reg_no_from_file(self, path):
        text = self.doctr_ocr.extract_text(path)
        reg_no = find_reg_no(text)
        if reg_no:
            return reg_no
        
        # Try pytesseract if doctr fails
        text = self.tesseract_ocr.extract_text(path)
        reg_no = find_reg_no(text)
        if reg_no:
            return reg_no
        
        return "No reg no. found"

def extract_reg_no_from_folder(root_folder):
    extractor = RegNoExtractor()
    for sub in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, sub)
        if not os.path.isdir(subfolder_path) or sub.startswith('_'):
            continue

        found = None
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                found = extractor.extract_reg_no_from_file(file_path)
                if found != "No reg no. found":
                    break
        print(f"{sub} - {found}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", required=True, help="Root directory containing subfolders of images/pdfs")
    args = parser.parse_args()
    extract_reg_no_from_folder(args.indir)


