from transformers import pipeline
from flask import Flask, render_template, request
import webbrowser
import threading
import os
import fitz  # PyMuPDF
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def format_summary(summary, style):
    if style == "paragraph":
        return summary
    elif style == "bullets":
        return "\n".join(f"• {s.strip()}" for s in summary.split('. ') if len(s.strip()) > 10)
    elif style == "keywords":
        words = [w.strip('.,') for w in summary.split() if len(w) > 5]
        keywords = list(set(words))[:10]
        return "Keywords: " + ", ".join(keywords)
    elif style == "headings":
        return f"Summary:\n\n1. {summary[:len(summary)//2]}...\n\n2. {summary[len(summary)//2:]}"
    else:
        return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    input_len = 0
    input_text = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        summary_style = request.form.get('summary_style', 'paragraph')
        length_option = request.form.get('summary_length', 'medium')

        file = request.files.get('pdf_file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            input_text = extract_text_from_pdf(filepath)

        input_len = len(input_text.strip())
        if input_text.strip():
            max_len = 130 if length_option == "short" else 250 if length_option == "medium" else 500
            input_text = input_text[:3000]
            summary_output = summarizer(input_text, min_length=30, max_length=max_len, do_sample=False)
            summary = format_summary(summary_output[0]['summary_text'], summary_style)

    return render_template('index.html', summary=summary.strip(), input_len=input_len, input_text=input_text)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
