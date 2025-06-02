from doctr import io
from doctr.models import ocr_predictor

class DoctrOCR:
    def __init__(self):
        self.model = ocr_predictor(pretrained=True)

    def extract_text(self, path: str) -> str:
        try:
            if path.lower().endswith(('.jpg', '.jpeg', '.png')):
                doc = io.DocumentFile.from_images([path])
            elif path.lower().endswith('.pdf'):
                doc = io.DocumentFile.from_pdf(path)
            else:
                return ""
            result = self.model(doc)
            return " ".join(
                word.value
                for page in result.pages
                for block in page.blocks
                for line in block.lines
                for word in line.words
            )
        except Exception:
            return ""


