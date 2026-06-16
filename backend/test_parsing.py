import asyncio
import io
from fastapi import UploadFile
from app.services.file_service import extract_text
import fitz # PyMuPDF
from docx import Document

async def run_tests():
    # 1. Create a dummy PDF
    pdf_doc = fitz.open()
    page = pdf_doc.new_page()
    page.insert_text((50, 50), "Hello PDF Resume")
    pdf_bytes = pdf_doc.write()
    pdf_doc.close()
    
    # Test PDF
    pdf_file = UploadFile(filename="test.pdf", file=io.BytesIO(pdf_bytes))
    pdf_text = await extract_text(pdf_file)
    print("PDF Text:", pdf_text.strip())
    assert "Hello PDF Resume" in pdf_text
    
    # 2. Create a dummy DOCX
    docx_doc = Document()
    docx_doc.add_paragraph("Hello DOCX Resume")
    docx_io = io.BytesIO()
    docx_doc.save(docx_io)
    docx_bytes = docx_io.getvalue()
    
    # Test DOCX
    docx_file = UploadFile(filename="test.docx", file=io.BytesIO(docx_bytes))
    docx_text = await extract_text(docx_file)
    print("DOCX Text:", docx_text.strip())
    assert "Hello DOCX Resume" in docx_text
    
    print("All extraction tests passed!")

if __name__ == "__main__":
    asyncio.run(run_tests())
