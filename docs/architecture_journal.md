# Project Ascend - Architecture Journal

---

# Date
03 August 2026

---

# Sprint

Sprint 1

---

# Feature

Streaming AI Responses

---

# Client Requirement

Users say the chatbot feels slow because nothing appears while the AI is generating.

---

# Business Understanding

## Problem

Users experience a blank screen for several seconds while waiting for the AI response.

Although the backend is working correctly, users perceive the application as frozen.

---

## Questions Asked

Q: Does every user experience this?

A: Yes.

---

Q: Does it happen for every response?

A: Yes. Long responses simply make the issue more noticeable.

---

Q: What happens because of this?

A:

- Users think the application froze.
- Some users refresh the page.
- Some users click Send multiple times.

---

Q: When did users begin reporting this?

A:

After the chatbot feature was released.

---

# Requirements Discovered

- Backend currently waits until the entire AI response is generated.
- Users see nothing while waiting.
- Users perceive the application as frozen.
- Client wants responses to begin appearing immediately.
- Client does not care how it is implemented.

---

# Architecture Discussion

## Decision Needed

Should we:

Option A

Modify the existing `/chat` endpoint to stream responses?

or

Option B

Create a new endpoint dedicated to streaming?

---

## My Thoughts

(To be written by me.)
I think the same api, but wait we can actually have a new api endpoint and use /chat for just testing prupose. but i don't know what that means and how it can be achieved according to my developer knowledge.

---

# Architect's Feedback

(To be filled after discussion.)
Decision:
Create a new endpoint:

POST /chat/stream

Reasoning:

- Preserve the existing /chat API contract.
- Maintain backward compatibility for existing clients.
- Allow gradual adoption of streaming.
- Deprecate /chat in the future only if appropriate after users have migrated.

---

# Developer Tasks

(To be decided later.)

---

# Lessons Learned

- Business Analysts investigate problems before proposing solutions.
- Architects make important technical decisions.
- Users often care more about perceived performance than actual latency.

---

# Open Questions

(To revisit later.)


# Sprint Backlog

## Story 1
Title: Add Gemini Streaming Support
Status: Completed

## Story 2
Title: Add Streaming Provider Routing
Status: Completed

## Story 3
Title: Create /chat/stream Endpoint
Status: Completed

## Story 4
Title: Persist Conversation After Stream Completes
Status: Completed

---

# Sprint Summary

## Completed

- Implemented Gemini streaming.
- Added provider streaming support.
- Introduced `/chat/stream`.
- Preserved `/chat`.
- Introduced `conversation_service.py`.
- Implemented streamed conversation persistence.
- Verified conversation history.
- Verified streaming endpoint.

---

## Architecture Decisions Made

- Introduced a dedicated streaming endpoint instead of modifying `/chat`.
- Introduced `conversation_service.py` to separate conversation workflow from the API layer.
- Kept provider-specific logic inside provider services.
- Kept API layer thin.

---

## Challenges Faced

- Understanding generators and `yield`.
- Understanding streaming responsibilities.
- Designing layer responsibilities.
- Swagger could not properly demonstrate streaming.
- Bruno buffered streamed responses even though backend streaming worked correctly.

---

## Future Improvements

- Add Groq streaming.
- Add streaming fallback.
- Improve streaming client testing.