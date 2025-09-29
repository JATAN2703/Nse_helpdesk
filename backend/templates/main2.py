from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pdfplumber
import os

app = Flask(__name__)

# Allow upload of PDF files
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            extract_text(filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')

def extract_text(filename):
    with pdfplumber.open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        # You can process the extracted text as needed.
        # For example, save it to a file or store it in a database.
        with open('text_summaries/' + filename + '.txt', 'w') as f:
            f.write(text)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('text_summaries'):
        os.makedirs('text_summaries')
    app.run(debug=True)