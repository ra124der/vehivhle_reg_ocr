import shutil
import logging
import os

logger = logging.getLogger(__name__)

# Try to find Tesseract in PATH
pytesseract_path = shutil.which("tesseract")
if not pytesseract_path or not os.path.exists(pytesseract_path):
    logger.warning(" Tesseract is not in system PATH.")

# Try to find Poppler's pdftoppm in PATH
poppler_bin = shutil.which("pdftoppm")
poppler_path = os.path.dirname(poppler_bin) if poppler_bin else None
if not poppler_path or not os.path.exists(poppler_path):
    logger.warning("  Poppler (pdftoppm) is not in system PATH.")



