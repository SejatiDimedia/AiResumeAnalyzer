import io
import fitz  # PyMuPDF
from docx import Document
from fastapi import UploadFile, HTTPException

async def extract_text(file: UploadFile) -> str:
    """
    Extracts text from an uploaded PDF or DOCX file.
    Validates the file type before parsing.
    """
    filename = file.filename or ""
    content_type = file.content_type
    
    # Check by extension or MIME type
    is_pdf = filename.lower().endswith(".pdf") or content_type == "application/pdf"
    is_docx = (
        filename.lower().endswith(".docx") or 
        content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    
    if not (is_pdf or is_docx):
        raise HTTPException(status_code=415, detail="Unsupported file format. Please upload a PDF or DOCX file.")
    
    # Read the file content into memory
    content = await file.read()
    
    if is_pdf:
        return _extract_pdf(content)
    elif is_docx:
        return _extract_docx(content)
    
    raise HTTPException(status_code=415, detail="Unsupported file format.")

def _extract_pdf(content: bytes) -> str:
    try:
        # Open the PDF from bytes
        doc = fitz.open(stream=content, filetype="pdf")
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()
        return "\n".join(text_parts).strip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse PDF file. The file might be corrupt. Error: {str(e)}")

def _extract_docx(content: bytes) -> str:
    try:
        # Open the DOCX from bytes
        doc = Document(io.BytesIO(content))
        text_parts = [para.text for para in doc.paragraphs]
        return "\n".join(text_parts).strip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse DOCX file. The file might be corrupt. Error: {str(e)}")
