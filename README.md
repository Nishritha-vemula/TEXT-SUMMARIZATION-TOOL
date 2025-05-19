# TEXT-SUMMARIZATION-TOOL

"COMPANY": CODTECH IT SOLUTIONS

"NAME": NISHRITHA VEMULA

"INTERN ID": CODF274

"DOMAIN": ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

"DURATION": 4 WEEKS

"MENTOR" : NEELA SANTOSH 

#  AI Text Summarizer

A web-based AI-powered text summarization tool built with **Flask**, **Transformers**, and **PyMuPDF** that allows users to generate concise summaries from **plain text** or **PDF files**. The application features a clean and responsive user interface, supports multiple summary styles, and includes advanced options for summary length control.

---

##  Features

 **Input Flexibility**

* Enter or paste raw text into a textarea
* Upload PDF files (text extracted automatically using PyMuPDF)

 **Customizable Summary Output**

* Choose from four summary styles:

  * **Paragraph**
  * **Bulleted List**
  * **Keywords**
  * **Subheadings**

 **Summary Length Control**

* Short (\~130 words)
* Medium (\~250 words)
* Long (\~500 words)

 **Live Character Counter**

* Displays input length in real-time

 **Dark Mode Toggle**

* Easy on the eyes for extended usage

 **Responsive & Clean UI**

* Works well on both desktop and tablet screens
* Clean design using pure CSS for professional look and feel

 **Copy to Clipboard**

* One-click copy functionality for generated summary

---

##  Tech Stack

* **Backend**: Flask (Python)
* **NLP Model**: [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) via Hugging Face Transformers
* **PDF Text Extraction**: [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
* **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **requirements.txt**

```
Flask
transformers
torch
PyMuPDF
```

### 3. Run the app

```bash
python app.py
```

The app will open automatically in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##  Folder Structure

```
🔹 app.py
🔹 styled_transfer.py (if needed)
🔹 static/
├── uploads/
└── styles.css
🔹 templates/
└── index.html
🔹 requirements.txt
```

---

##  Screenshots

![Image](https://github.com/user-attachments/assets/84fb69f6-f735-46a2-81ee-2ee6df7f985b)

---

##  Use Cases

* Quickly summarize long articles, reports, or PDFs
* Extract key insights from research papers
* Convert raw input into digestible points or executive summaries
* Ideal for students, journalists, researchers, and content creators

---

##  Attribution

Model used: [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) by Meta
PDF Parsing via: [PyMuPDF](https://pymupdf.readthedocs.io/)

---

## 📬 Feedback & Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

If you found this helpful, give it a ⭐ on GitHub!
