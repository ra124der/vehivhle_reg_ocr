import logging
from doctr import io
from doctr.models import ocr_predictor

logger = logging.getLogger(__name__)

# Always assume doctr is available
doctr_model = ocr_predictor(pretrained=True)

def extract_text_doctr(path):
    try:
        if path.lower().endswith(('.jpg', '.jpeg', '.png')):
            doc = io.DocumentFile.from_images([path])
        elif path.lower().endswith('.pdf'):
            doc = io.DocumentFile.from_pdf(path)
        else:
            return ""

        result = doctr_model(doc)
        return " ".join(
            word.value
            for page in result.pages
            for block in page.blocks
            for line in block.lines
            for word in line.words
        )
    except Exception as e:
        logger.error(f"DocTR failed on {path}: {e}")
        return None




