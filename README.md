# Project Ascend

Project Ascend is a long-term engineering project focused on becoming a strong Backend and AI Engineer through real-world software development.

The goal is not simply to build an AI chatbot, but to learn professional software engineering practices including:

- Backend Development
- API Design
- AI Integration
- Software Architecture
- System Design
- Git Workflow
- Engineering Documentation
- Design Decisions
- Clean Code
- Product Thinking

---

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- Groq API
- Git
- GitHub

---

## Features Completed

### Sprint 1

- AI Chat Endpoint
- Streaming Endpoint
- Gemini Streaming
- Conversation Persistence
- Architecture Decision Record (ADR)
- Conversation Service Layer

### Sprint 2

- Native Groq SDK Integration
- Groq Streaming Support
- Provider Routing
- Gemini → Groq Streaming Fallback
- Unified Provider Interface

---

## Current Architecture

```
Client
    │
    ▼
main.py
    │
    ▼
conversation_service.py
    │
    ▼
service.py
   ├──────────────┐
   ▼              ▼
gemini_service.py groq_service.py
```

---

## Documentation

See the `/docs` folder for:

- Architecture Journal
- Sprint Backlog
- Sprint Reviews
- Architecture Decision Records

---

## Status

Current Sprint:

Sprint 2 Complete