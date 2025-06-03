import logging
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

logger = logging.getLogger(__name__)

def preprocessimg(img):
    img = img.convert('L')
    img = img.resize((img.width * 2, img.height * 2))
    return img

def extract_text_pytesseract(path, poppler_path, tesseract_cmd):
    try:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        if path.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = preprocessimg(Image.open(path))
            return pytesseract.image_to_string(img)
        elif path.lower().endswith('.pdf'):
            full_text = ""
            images = convert_from_path(path, poppler_path=poppler_path)
            for img in images:
                img = preprocessimg(img)
                full_text += pytesseract.image_to_string(img)
            return full_text
    except Exception as e:
        logger.error(f"Tesseract failed on {path}: {e}")
        return ""



