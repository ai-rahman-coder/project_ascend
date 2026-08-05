# Project Ascend Journey

## Purpose

This document tracks how my engineering thinking evolves throughout Project Ascend.

The goal is not only to build software but to become better at architecture, product thinking, business understanding, and technical decision making.

---

## Sprint 1

### What changed in my thinking

- I learned to separate responsibilities before writing code.
- I understood why API contracts should be preserved.
- I started thinking in layers instead of functions.
- I realized architecture decisions are often more important than implementation details.
- I learned that streaming is an end-to-end feature, not just an SDK feature.

### Biggest Challenges

- Understanding generators and `yield`.
- Understanding where responsibilities belong.
- Distinguishing architecture from implementation.

### Biggest Takeaway

Always decide **who owns the responsibility** before deciding **how to implement it**.


---

## Sprint 2

### What changed in my thinking

- I realized the value of a stable provider contract. Because Gemini and Groq expose the same interface, the rest of the application remained unchanged.
- I started thinking about how architecture reduces the amount of code that needs to change when new features are introduced.
- I became more comfortable implementing features by recognizing patterns instead of asking for implementation details.
- I learned that introducing a new provider should require changes only in the provider layer and the orchestration layer.

### Biggest Challenges

- Understanding how streaming fallback should work.
- Deciding where the full streamed response should be assembled.
- Separating provider responsibilities from conversation responsibilities.
- Distinguishing between architecture decisions and implementation decisions.

### Biggest Takeaway

Good architecture reduces stress.

During this sprint I noticed that instead of wondering "what else will break?", I naturally started asking "which layer owns this responsibility?". That change in thinking allowed me to implement Groq streaming with very few code changes.

### Engineering Milestones

- Migrated Groq from the OpenAI-compatible Responses API to the native Chat Completions API.
- Implemented Groq streaming.
- Added Gemini → Groq streaming fallback.
- Verified that the provider abstraction worked without modifying the API layer or conversation workflow.


---

## Sprint 3

### What changed in my thinking

- I learned that logging is part of system observability, not debugging.
- I understood how Python's logging hierarchy works through loggers, handlers and formatters.
- I realized logging should describe business events instead of printing arbitrary values.
- I became more conscious about where logging responsibilities belong.

### Biggest Challenges

- Understanding the difference between `basicConfig()` and `dictConfig()`.
- Understanding why Uvicorn logging changed after introducing my own logging configuration.
- Deciding what should and should not be logged.

### Biggest Takeaway

Logging is another architectural layer.

A good log should explain **what the application is doing**, not simply **what the code executed**.

### Engineering Milestones

- Introduced centralized logging configuration.
- Added structured log formatting.
- Added application logs throughout the conversation workflow.
- Logged provider selection and provider fallback.
- Removed `print()` based debugging.