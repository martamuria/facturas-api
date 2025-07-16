
import pdfplumber
import pytesseract
from PyPDF2 import PdfReader
import io

def extract_invoice(pdf_bytes: bytes) -> dict:
    text = ""
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    result = {
        "emisor": "Desconocido",
        "fecha": "Sin detectar",
        "importe": "0.00 €",
        "texto_completo": text[:1000]
    }
    return result
