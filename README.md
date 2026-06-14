# ⚖️ Mini LegalX AI Knowledge Centre

## 🚀 Live Demo
https://huggingface.co/spaces/Hemasivakavi/legalx-ai

---

## 📌 Project Overview

LegalX AI Knowledge Centre is an **AI-powered legal assistant system** that converts complex legal documents into simple, structured, and easy-to-understand knowledge cards.

It uses **Retrieval-Augmented Generation (RAG)** to answer legal questions based only on uploaded legal documents.

The system helps users understand laws in a simplified format without legal complexity.

---

## 📄 Documents Used

The system is trained and tested on multiple Indian legal documents:

- Right to Information Act (RTI)
- Consumer Protection Act
- POCSO Act
- Cyber Crime Laws
- GST Registration Rules

---

## ✨ Key Features

### 📚 1. Legal Knowledge Cards
- Displays legal topics in structured cards
- Each card includes:
  - Topic Name
  - Short Description
  - Read More option

---

### 🧠 2. AI Legal Summarization
- Converts legal documents into:
  - Summary (simple explanation)
  - Key Rights
  - Important Provisions
  - Important Penalties
  - Who Can Benefit

---

### 🔍 3. Retrieval-Augmented Generation (RAG)
- Uses FAISS vector database
- Retrieves most relevant legal chunks
- Ensures AI answers are based only on documents

---

### 💬 4. AI Chat System
- Ask questions about any legal topic
- Answers generated only from document context
- Prevents hallucination

---

### 🔊 5. Audio Summary Feature
- Converts legal summaries into speech
- Uses Google Text-to-Speech (gTTS)
- Helps accessibility and learning

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS (Vector Search)
- Sentence Transformers (BGE model)
- Google Gemini API
- gTTS (Text-to-Speech)

---

## ⚙️ System Architecture

Legal Document → Chunking → Embeddings → FAISS Index  
→ User Query → Retrieval → Gemini AI → Structured Answer  
→ Streamlit UI → Audio Output

---

## 📂 Project Structure

LegalX_Knowledge_Centre/
│
├── app.py
├── legalx_ai.py
├── legalx_backend.py
├── legalx_chat.py
├── retriever.py
├── audio_utils.py
├── cards.py
├── utils.py
│
├── vector_store/
│ ├── legalx_faiss.index
│ ├── chunks.pkl
│ ├── metadata.pkl
│
├── data/
│ ├── rti.pdf
│ ├── pocso.pdf
│ ├── cybercrime.pdf
│ ├── gst.pdf
│
└── requirements.txt


---

## 🚀 Deployment

- Deployed using **Hugging Face Spaces**
- Streamlit frontend
- Python backend with FAISS + Gemini API

---

## 📌 How It Works

1. User selects a legal topic  
2. System retrieves relevant document chunks  
3. AI generates structured legal summary  
4. User can:
   - Read summary
   - Ask questions
   - Listen audio explanation  

---

## 🎯 Use Cases

- Legal education
- Law students
- Public awareness
- Government scheme understanding
- Quick legal consultation support

---

## ⚠️ Note

- AI responses are based only on provided documents
- No external legal advice is given
- System prevents hallucinated answers using RAG

---

## 👨‍💻 Author

Developed by: **Hemasivakavi**

---

## ⭐ Live Project

👉 https://huggingface.co/spaces/Hemasivakavi/legalx-ai
