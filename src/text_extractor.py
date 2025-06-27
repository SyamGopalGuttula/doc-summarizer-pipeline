import pdfplumber
import docx
from pdf2image import convert_from_path
import pytesseract
import os
import tempfile

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    if text.strip():  # If regular text was found, return it or else it will fall back to OCR
        return text.strip()
    else:
        # Fallback to OCR
        return extract_text_from_pdf_ocr(file_path)

def extract_text_from_pdf_ocr(file_path):
    text = ""
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(file_path, output_folder=path)
        for image in images:
            text += pytesseract.image_to_string(image)
    return text.strip()


def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only .pdf and .docx are supported.")
