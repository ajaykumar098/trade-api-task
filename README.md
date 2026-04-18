# Trade Opportunities API

## 🚀 Run Project

pip install -r requirements.txt
uvicorn app.main:app --reload

## 🔐 Authentication
Header:
x-api-key: mysecurekey

## 📊 Endpoint
GET /analyze/{sector}

Example:
http://127.0.0.1:8000/analyze/technology

## 📌 Features
- FastAPI backend
- Gemini AI integration
- Dynamic markdown report
- Rate limiting
- API key authentication
- Input validation
- In-memory session tracking
