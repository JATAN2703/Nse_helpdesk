from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Define a route for uploading PDF files
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('/path/to/pdf/storage', filename))
        return 'File uploaded successfully'

# Define a route for retrieving PDF files
@app.route('/pdf/<string:filename>', methods=['GET'])
def get_pdf(filename):
    return send_from_directory('/path/to/pdf/storage', filename)

if __name__ == '__main__':
    app.run(debug=True)