import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from enb import pytesseract_path, poppler_path

# Set tesseract_cmd only if path is provided
if pytesseract_path:
    pytesseract.pytesseract.tesseract_cmd = pytesseract_path

class TesseractOCR:
    def preprocess_img(self, img):
        img = img.convert('L')
        return img.resize((img.width * 2, img.height * 2))

    def extract_text(self, path: str) -> str:
        try:
            if path.lower().endswith(('.jpg', '.jpeg', '.png')):
                img = self.preprocess_img(Image.open(path))
                return pytesseract.image_to_string(img)
            elif path.lower().endswith('.pdf'):
                images = convert_from_path(path, poppler_path=poppler_path) if poppler_path else convert_from_path(path)
                return "".join(
                    pytesseract.image_to_string(self.preprocess_img(img))
                    for img in images
                )
        except Exception:
            return ""
        return ""

