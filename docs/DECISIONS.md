# Engineering Decisions

This document records important engineering decisions made throughout Project Ascend.

Unlike ADRs, these decisions are lightweight and focus on the reasoning behind implementation choices.

---

# Decision 001

## Title

Introduce `conversation_service.py`

### Context

Initially, the API endpoints (`main.py`) were responsible for:

- Receiving HTTP requests
- Managing conversation history
- Calling AI providers
- Returning responses

This mixed HTTP concerns with application workflow.

### Decision

Introduce a dedicated `conversation_service.py`.

### Reason

- Keep `main.py` focused on HTTP only.
- Centralize conversation workflow.
- Make both `/chat` and `/chat/stream` reuse the same business layer.
- Make future changes independent of the API framework.

### Result

Responsibilities became:

```
main.py
    ↓
conversation_service.py
    ↓
service.py
    ↓
provider
```

---

# Decision 002

## Title

Keep provider routing inside `service.py`

### Context

The application supports multiple AI providers.

A decision was needed regarding where provider selection and fallback should occur.

### Decision

Provider routing belongs inside `service.py`.

### Reason

- The API should not know which provider is used.
- Conversation management should not know which provider is used.
- Provider implementations should remain independent.

### Result

Adding or replacing providers only requires changes inside the orchestration layer.

---

# Decision 003

## Title

Keep provider implementations isolated

### Context

Gemini and Groq expose different SDKs.

Without abstraction, SDK-specific code would spread across the project.

### Decision

Each provider owns its own implementation.

Examples:

- `gemini_service.py`
- `groq_service.py`

### Reason

- Hide SDK differences.
- Keep provider-specific code isolated.
- Make replacing providers easier.

### Result

The rest of the project communicates through a common provider interface instead of SDK-specific code.

---

# Decision 004

## Title

Preserve a common provider contract

### Context

Both Gemini and Groq should behave identically from the application's perspective.

### Decision

Every provider returns the same response structure and exposes equivalent streaming functions.

### Reason

A common contract allows the orchestration layer to remain unchanged regardless of the underlying provider.

### Result

Introducing Groq required almost no changes outside the provider layer.

---

# Decision 005

## Title

Use Groq's native Chat Completions API

### Context

Groq offers both an OpenAI-compatible Responses API and a native Chat Completions API.

The Responses API did not support streaming.

### Decision

Use the native Chat Completions API.

### Reason

- Supports streaming.
- Matches the project requirements.
- Keeps provider capabilities consistent.

### Result

Groq now supports both normal and streaming responses.

---

# Decision 006

## Title

Implement provider fallback inside the orchestration layer

### Context

Users should continue receiving responses when Gemini exceeds its quota.

### Decision

Implement Gemini → Groq fallback inside `service.py`.

### Reason

Only the orchestration layer should decide which provider executes a request.

### Result

The API layer and conversation workflow remained unchanged while fallback support was added.

---

# Decision 007

## Title

Validate architecture through change impact

### Context

After implementing Groq streaming, an important observation was made.

### Observation

Supporting a second provider required modifications only in:

- `groq_service.py`
- `service.py`

No changes were required in:

- `main.py`
- `conversation_service.py`
- `conversation.py`

### Conclusion

This validated that responsibilities were correctly separated and the architecture scaled as intended.


---

# Decision 008

## Title

Centralize application logging

### Context

Logging was beginning to appear across multiple modules.

Without a common configuration, formatting and behavior would become inconsistent.

### Decision

Introduce a centralized logging configuration and allow every module to obtain its own logger using:

```python
logger = logging.getLogger(__name__)
```

### Reason

- Consistent log format.
- Single logging configuration.
- Module-specific log names.
- Easier future migration to file logging or external logging systems.

### Result

Every module now produces consistent logs while remaining independently identifiable.