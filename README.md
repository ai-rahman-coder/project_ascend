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
- Engineering Decision Making
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
- Conversation Service Layer
- Streaming Architecture

### Sprint 2

- Native Groq SDK Integration
- Groq Streaming Support
- Provider Routing
- Gemini → Groq Streaming Fallback
- Unified Provider Interface

### Sprint 3

- Centralized Logging Configuration
- Structured Application Logging
- Conversation Workflow Logging
- Provider Activity Logging
- Provider Fallback Logging

---

## Current Architecture

```text
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

The `docs/` directory contains:

- `ROADMAP.md` – Overall learning roadmap
- `JOURNEY.md` – Engineering growth throughout Project Ascend
- `architecture_journal.md` – Architectural analysis for each sprint
- `engineering_decisions.md` – Important engineering decisions
- `architecture/adr/` – Architecture Decision Records (ADRs)
- `user_guide/` – User documentation (planned)

---

## Current Status

- ✅ Sprint 1 Complete
- ✅ Sprint 2 Complete
- ✅ Sprint 3 Complete

**Current Focus**

Sprint 4 – Exception Handling & Error Management