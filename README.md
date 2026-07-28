# 🏥 MediAssist AI

> An AI-powered Healthcare Assistant built using **Python, Streamlit, Groq Llama 3.3, LangChain, Hugging Face Embeddings, and FAISS**. The application provides educational healthcare information using Retrieval-Augmented Generation (RAG), conversation memory, emergency symptom detection, and source citations.

---

## 📌 Overview

MediAssist AI is an intelligent healthcare chatbot designed to provide reliable and educational health information. It leverages Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) to answer user queries using a curated healthcare knowledge base.

⚠️ **Disclaimer:** This application is intended for educational purposes only. It is **not a substitute for professional medical advice, diagnosis, or treatment.**

---

## ✨ Features

- 🤖 AI-powered healthcare chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 Conversation memory
- 🚨 Emergency symptom detection
- 📖 Source-based responses
- 💬 Suggested healthcare questions
- ⚡ Fast responses using Groq Llama 3.3
- 🎨 Interactive Streamlit interface
- 🔒 Prompt engineering with safety guardrails

---

## 🏗️ System Architecture

```
                  User
                    │
                    ▼
            Streamlit Interface
                    │
                    ▼
        Emergency Symptom Detection
                    │
                    ▼
          Conversation Memory
                    │
                    ▼
              RAG Pipeline
      ┌──────────────────────────┐
      │ Healthcare Knowledge Base│
      │      + FAISS Index       │
      └──────────────────────────┘
                    │
                    ▼
          Prompt Engineering
                    │
                    ▼
        Groq Llama 3.3-70B Model
                    │
                    ▼
        AI Response + References
```

---

# 📂 Project Structure

```
MediAssist-AI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   └── medical_docs/
│
├── llm/
│   └── gemini.py
│
├── memory/
│   └── memory.py
│
├── prompts/
│   └── prompt.py
│
├── rag/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── safety/
│   └── emergency.py
│
├── tests/
│
└── assets/
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Frontend

- Streamlit

### Large Language Model

- Groq API
- Llama 3.3 70B Versatile

### AI Frameworks

- LangChain
- Hugging Face Sentence Transformers

### Vector Database

- FAISS

### Embedding Model

- all-MiniLM-L6-v2

### Other Libraries

- python-dotenv
- NumPy
- Pandas

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/jb-123-ctrl/MediAssist-AI.git
```

Go to the project folder

```bash
cd MediAssist-AI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 💡 Example Questions

- What are the symptoms of diabetes?
- How can I reduce high blood pressure?
- What should I do for a minor burn?
- What foods help improve immunity?
- Explain hypertension.
- What are the symptoms of dengue?

---

# 🚨 Emergency Detection

The chatbot detects emergency symptoms such as:

- Chest pain
- Difficulty breathing
- Stroke symptoms
- Seizures
- Severe bleeding
- Loss of consciousness

If emergency keywords are detected, the chatbot advises the user to seek immediate medical attention before providing educational information.

---

# 📚 Retrieval-Augmented Generation (RAG)

The chatbot uses a healthcare knowledge base stored locally.

Workflow:

```
User Query
     │
     ▼
Embedding Generation
     │
     ▼
FAISS Similarity Search
     │
     ▼
Relevant Documents
     │
     ▼
Prompt Engineering
     │
     ▼
Groq Llama 3.3
     │
     ▼
Final Response with References
```

---

# 🔒 Safety Features

- No medical diagnosis
- No prescription generation
- Educational responses only
- Emergency symptom detection
- Professional medical disclaimer
- Source-based answers

---

# 📸 Screenshots

Add screenshots here.

```
screenshots/
    home.png
    chat.png
    sidebar.png
```

Example:

```markdown
![Home](screenshots/home.png)
![Chat](screenshots/chat.png)
```

---

# 🎯 Future Improvements

- Voice interaction
- Multi-language support
- User authentication
- Medical PDF upload
- Cloud deployment
- Chat history database
- Doctor appointment integration
- OCR-based prescription reading

---

# 👨‍💻 Developer

**Jayabharathi S**

AI & Data Analytics Engineer

GitHub:
https://github.com/jb-123-ctrl

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful,

⭐ Star the repository

🍴 Fork the repository

🤝 Contributions are welcome!

---

## 📬 Contact

For questions or collaboration:

GitHub: https://github.com/jb-123-ctrl

---

## 🙏 Acknowledgements

- Groq
- Meta Llama
- LangChain
- Hugging Face
- FAISS
- Streamlit
