# VoxaAI – AI-Powered Customer Support Voice Agent

VoxaAI is an end-to-end **AI-powered voice-based customer support system** that handles
real-time phone calls using **Twilio**, **FastAPI**, **LLMs**, and
**Retrieval-Augmented Generation (RAG)**.

The system can answer general customer queries, fetch order/delivery/return/refund
status from a database, and maintain multi-turn conversational context.

---

## Tech Stack

- **Backend**: Python, FastAPI
- **LLM**: Groq (LLaMA models)
- **Voice Interface**: Twilio Voice API
- **Database**: MongoDB
- **RAG**: FAISS + SentenceTransformers
- **Embeddings**: all-MiniLM-L6-v2
- **Local Tunneling**: ngrok

---

## System Architecture

1. User calls a Twilio phone number  
2. Twilio converts speech → text  
3. Request is sent to FastAPI via public webhook (ngrok)  
4. Intent is detected:
   - Order-related → Database Agent
   - General query → RAG + LLM
5. AI response is converted to speech and played back to the user  

---

## Key Features

- 📞 Voice-based AI customer support
- 🧠 Context-aware multi-turn conversations
- 📦 Order, delivery, return & refund handling
- 🔍 RAG-based knowledge retrieval
- ⚡ Low-latency LLM responses
- 🗂️ Modular, production-style backend architecture

---



## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/affanrahman0/voxaAI-customer-support-agent.git
cd voxaAI-customer-support-agent

###2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # Windows

###3. Install dependencies
pip install -r requirements.txt

###4. Environment variables

Create a .env file using .env.example:

MONGODB_URI=your_mongodb_uri
GROQ_API_KEY=your_groq_api_key

###5. Build the vector database (RAG)
python backend/rag/build_support_vectordb.py

###6. Run the FastAPI server
uvicorn app:app --reload


The server will run on:

http://localhost:8000

🔊 Twilio Voice + ngrok Setup (Required)

Twilio requires a public URL, so ngrok is used for local development.

1. Install ngrok

Download from:

https://ngrok.com/download


Extract it (example path: C:\ngrok\ngrok.exe).

2. Expose local server

In a new terminal window:

C:\ngrok\ngrok.exe http 8000


You will see:

Forwarding https://abcd-1234.ngrok-free.app -> http://localhost:8000

3. Configure Twilio Webhook

In Twilio Console → Phone Numbers → Voice:

A CALL COMES IN:

https://abcd-1234.ngrok-free.app/twilio/voice


Method: POST

4. Test the system

Call your Twilio phone number and speak naturally.
The AI will respond in real time using voice.
