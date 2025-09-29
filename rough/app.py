from flask import Flask, render_template, request
import os
import io
from PyPDF2 import PdfFileReader
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.llms import OpenAI

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('pdfs')
        summaries = {}
        for pdf in uploaded_files:
            pdf_reader = PdfFileReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extractText()
            doc = Document(page_content=text)
            llm = OpenAI(temperature=0)
            chain = load_summarize_chain(llm, chain_type="map_reduce")
            summary = chain.run(doc)
            summaries[pdf.filename] = summary
        return render_template('index.html', summaries=summaries)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)