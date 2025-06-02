import os

# Get paths from environment variables, or None if not set
pytesseract_path = os.getenv("TESSERACT_PATH")
poppler_path = os.getenv("POPLER_PATH")

# Warn user if paths are invalid or missing
if not pytesseract_path or not os.path.exists(pytesseract_path):
    print(f"⚠️  Tesseract path is invalid or not set: {pytesseract_path}")

if not poppler_path or not os.path.exists(poppler_path):
    print(f"⚠️  Poppler path is invalid or not set: {poppler_path}")

