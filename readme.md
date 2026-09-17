# ✨ DIVA – Intelligent Document Analyzer RAG Chatbot

> Chat with your documents developed using strong concepts of Retrieval-Augmented Generation (RAG), semantic search, and Large Language Models.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

**DIVA** is a production-oriented **Retrieval-Augmented Generation (RAG)** application that enables users to interact conversationally with their documents.

Instead of manually reading lengthy PDFs or searching through hundreds of pages, users simply upload a document and ask questions in natural language. Doclyzer retrieves the most relevant document chunks using semantic search and generates grounded answers using a Large Language Model while providing page-based citations for transparency.

The application is designed with a modular architecture using **FastAPI**, **LangChain**, **ChromaDB**, **Hugging Face**, and **Streamlit**, making it easy to extend into enterprise-grade document intelligence systems.

The RAG pipeline evaluation is also performed upon retriever and generator. And the evaluation using **DeepEval** produced the following results 

**Retriever Evaluation:**
- Contextual Precision : 1.00
- Contextual Recall : 0.84
  
**Generator Evaluation:**
- Faithfulness : 0.86
- Answer Relevancy : 0.95

---

# ✨ Features

##  Document Processing

- Upload PDF, DOCX, and TXT documents
- Automatic document parsing
- Page-aware document loading
- Recursive intelligent chunking
- Metadata preservation
- Local document storage

---

##  Semantic Search

- Recursive Character Text Splitting
- Hugging Face Embeddings
- ChromaDB Vector Database
- Persistent Vector Storage
- Maximum Marginal Relevance (MMR) Retrieval
- Fast Semantic Search

---

##  Retrieval-Augmented Generation (RAG)

- Context-aware retrieval
- History-aware question rewriting
- Multi-turn conversations
- Grounded AI responses
- Hallucination prevention
- Mathematical reasoning over document data
- Source-aware answer generation

---

##  Source Attribution

Every generated response includes:

- Document name
- Page citations
- Retrieved source chunks

This enables users to verify every generated answer directly from the original document.

---

##  Modern User Interface

- Clean Streamlit interface
- Responsive layout
- Interactive chat experience
- Elegant document upload workflow
- Professional sidebar
- Modern AI-inspired design

---

#  System Architecture

```text
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
               FastAPI Backend
                      │
                      ▼
              Indexing Service
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Loader Service             Document Processor
        │                           │
        └─────────────┬─────────────┘
                      ▼
              Document Chunks
                      │
                      ▼
            Embedding Generation
                      │
                      ▼
            Chroma Vector Database
                      │
                      ▼
             MMR Semantic Retrieval
                      │
                      ▼
          History-aware Query Rewriter
                      │
                      ▼
                Qwen 2.5 LLM
                      │
                      ▼
         Grounded Response + Citations
```

---

#  Tech Stack

## Backend

- FastAPI
- LangChain
- ChromaDB
- Hugging Face Inference API

## Frontend

- Streamlit

## Embedding Model

- BAAI/bge-small-en-v1.5

## Large Language Model

- Qwen2.5-7B-Instruct

## Document Parsing

- PyMuPDF
- python-docx

## Vector Database

- ChromaDB

---

# 📂 Project Structure

```text
Document-Analyzer-RAGChatbot/

│
├── app/
│   ├── api/
│   ├── chains/
│   ├── core/
│   ├── frontend/
│   ├── models/
│   ├── prompts/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── data/
│   ├── documents/
│   ├── vector_db/
│   └── cache/
│
├── tests/
│
├── requirements.txt
├── run.py
└── README.md
```

---

#  RAG Workflow

```text
Upload Document
        │
        ▼
Loader Service
        │
        ▼
Document Processing
        │
        ▼
Recursive Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Chroma Vector Database
        │
        ▼
MMR Retrieval
        │
        ▼
Question Rewriting
        │
        ▼
Qwen 2.5 LLM
        │
        ▼
Grounded Response
        │
        ▼
Page Citations
```

---

#  Project Evolution

This project originally began as a **YouTube Video RAG Chatbot**, allowing users to chat with YouTube videos using transcript-based Retrieval-Augmented Generation.

The application was later **completely refactored** into a generic **Document Analyzer RAG Chatbot**, just by leveraging its architecture, modularity, and extensibility.

## Major Refactoring Highlights

- Replaced YouTube transcript ingestion with a generic Loader Service
- Added support for PDF, DOCX, and TXT documents
- Redesigned the indexing pipeline
- Refactored transcript processing into a reusable Document Processor
- Removed all YouTube-specific services, models, and APIs
- Introduced an Indexing Service for orchestration
- Redesigned the FastAPI API layer
- Updated the Streamlit frontend for document uploads
- Refactored prompts for document-grounded reasoning
- Replaced timestamp citations with page citations
- Simplified the RAG pipeline for single-document analysis
- Improved modularity for future multi-document support

This refactoring demonstrates how a domain-specific RAG application can be transformed into a reusable document intelligence platform.

---

# ▶️ Running the Backend

```bash
python run.py
```

Backend will be available at:

```
http://127.0.0.1:8000
```

---

# ▶️ Running the Frontend

```bash
streamlit run app/frontend/app.py
```

---

#  Current Capabilities

- Chat with uploaded documents
- PDF, DOCX, and TXT support
- Semantic document search
- Context-aware conversations
- History-aware retrieval
- MMR Retrieval
- Grounded AI responses
- Mathematical reasoning from document data
- Page-based citations
- Modular architecture
- Production-ready backend

---

# 🛣️ Future Roadmap

- Multiple document workspaces
- Cross-document querying
- Hybrid Retrieval (Dense + BM25)
- OCR support for scanned PDFs
- Table-aware document understanding
- AI-powered document summarization
- Docker deployment
- Cloud deployment
- Docker optimization
- Citation highlighting inside documents
- Export conversations to PDF

---

#  Screenshots

- Home Screen

  <img width="1918" height="979" alt="image" src="https://github.com/user-attachments/assets/0d74109c-8db0-4f39-a7cf-6facaebe9642" />

- Upload Document

  <img width="1919" height="1029" alt="image" src="https://github.com/user-attachments/assets/41469b68-0e0f-44e8-8edf-27dd1f1aaca1" />
  
- Chat Interface

  <img width="1919" height="1024" alt="image" src="https://github.com/user-attachments/assets/b5759a26-0700-4cc4-9586-fc0513752e09" />

- Page Citations

  <img width="675" height="131" alt="image" src="https://github.com/user-attachments/assets/80cea0a9-0a9f-4f9a-8592-679eba19d478" />


- Example Responses

  <img width="928" height="825" alt="image" src="https://github.com/user-attachments/assets/4d7cf053-340b-46fa-86e6-58534e907e34" />

- RAG Evaluation

  <img width="896" height="378" alt="Screenshot 2026-09-09 110536" src="https://github.com/user-attachments/assets/e5241363-49f5-49bb-a9bb-11daaf6b15ee" />

  <img width="1295" height="377" alt="Screenshot 2026-09-10 103405" src="https://github.com/user-attachments/assets/5b82c2cb-45c5-4e5e-b9d2-f99ebcf41844" />


# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
