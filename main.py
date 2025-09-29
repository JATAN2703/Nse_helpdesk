from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Endpoint to upload PDF files
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save the uploaded PDF file to a designated folder
    with open(f"pdf_folder/{file.filename}", "wb") as pdf_file:
        pdf_file.write(file.file.read())
    return JSONResponse(content={"message": "PDF uploaded successfully"})

# Endpoint to fetch a list of available PDFs
@app.get("/pdf-list/")
async def get_pdf_list():
    # List PDF files in the folder
    pdf_files = [f for f in os.listdir("pdf_folder") if f.endswith(".pdf")]
    return JSONResponse(content={"pdf_list": pdf_files})

# Endpoint to fetch the summary of a specific PDF
@app.get("/pdf-summary/{pdf_filename}")
async def get_pdf_summary(pdf_filename: str):
    # Extract and return summary for the given PDF
    # You may use a PDF parsing library like PyPDF2 or pdfminer
    # Replace the following line with your actual implementation
    summary = f"Summary for {pdf_filename}"
    return JSONResponse(content={"summary": summary})
