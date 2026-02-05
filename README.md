# Docu-Mind

**Docu-Mind** is a simple web app that lets you upload PDF or DOCX files and extract clean text from them.  
It also supports OCR for scanned documents.

---

## Features

- Upload **PDF** or **DOCX** files
- Extract text from documents
- OCR support for scanned PDFs or images
- Clean text output
- Files saved locally in `uploads/`

---

## Installation

**Clone the repository:**

**git clone https://github.com/pa-nuzz/docu-mind.git**  
**cd docu-mind**

---

## Creating and activating a virtual environment:

**python -m venv .venv**  
**source .venv/bin/activate**

---

## Installing dependencies:

**pip install -r requirements.txt**

---

## Starting the server:

**uvicorn app.main:app --reload**

**Open in browser:**  
**http://127.0.0.1:8000/**  

Upload a PDF or DOCX file to see the extracted text.
