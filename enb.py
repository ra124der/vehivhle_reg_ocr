import os
import logging

logger = logging.getLogger(__name__)

pytesseract_path = os.getenv("TESSERACT_PATH")
poppler_path = os.getenv("POPLER_PATH")

if not pytesseract_path or not os.path.exists(pytesseract_path):
    logger.warning(f"⚠️  Tesseract path is invalid or not set: {pytesseract_path}")

if not poppler_path or not os.path.exists(poppler_path):
    logger.warning(f"⚠️  Poppler path is invalid or not set: {poppler_path}")



