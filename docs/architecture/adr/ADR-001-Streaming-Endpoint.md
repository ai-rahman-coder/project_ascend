# ADR-001: Introduce a Dedicated Streaming Endpoint

## Status

Accepted

---

## Context

Users reported that the chatbot appeared frozen while waiting for AI responses.

The existing `POST /chat` endpoint returned a complete response only after the AI finished generating the entire answer.

We needed to introduce response streaming without disrupting existing functionality.

---

## Decision

Create a new endpoint:

```
POST /chat/stream
```

instead of modifying the existing:

```
POST /chat
```

---

## Alternatives Considered

### Option A — Modify `/chat`

**Pros**

- Only one endpoint to maintain.
- No duplicate API routes.

**Cons**

- Breaks the existing API contract.
- Existing clients would need to change their integration immediately.
- Higher deployment risk.

---

### Option B — Create `/chat/stream` (Chosen)

**Pros**

- Preserves backward compatibility.
- Existing clients continue using `/chat`.
- New clients can adopt streaming gradually.
- Lower deployment risk.

**Cons**

- Two endpoints must be maintained.
- Slightly larger API surface.

---

## Consequences

- Existing clients remain unaffected.
- Streaming can be adopted incrementally.
- The original endpoint may be deprecated in the future if all clients migrate.