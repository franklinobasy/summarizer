import logging

from fastapi import HTTPException, UploadFile

from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file: UploadFile) -> str:
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(file.file)
        text = " ".join(page.extract_text() for page in reader.pages)
        logging.info(f"{file.filename} successfully processed")
        return text
    except Exception as e:
        logging.error(f"Error encountered while processing {file.filename}")
        raise HTTPException(status_code=400, detail=f"Error reading PDF file: {e}")

def extract_text_from_docx(file: UploadFile) -> str:
    """Extract text from a DOCX file."""
    try:
        doc = Document(file.file)
        text =  " ".join(paragraph.text for paragraph in doc.paragraphs)
        logging.info(f"{file.filename} successfully processed")
        return text
    except Exception as e:
        logging.error(f"Error encountered while processing {file.filename}")
        raise HTTPException(status_code=400, detail=f"Error reading DOCX file: {e}")