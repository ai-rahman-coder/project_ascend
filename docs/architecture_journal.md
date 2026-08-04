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


---

# Date

04 August 2026

---

# Sprint

Sprint 2

---

# Feature

Groq Streaming and Provider Fallback

---

# Client Requirement

The application should continue responding even if the primary AI provider becomes unavailable due to rate limits.

Streaming behavior should remain unchanged regardless of which provider generates the response.

---

# Business Understanding

## Problem

The chatbot depended entirely on Gemini.

If Gemini exceeded its quota, streaming stopped and the user received an error.

---

## Requirements Discovered

- Streaming should continue even when the primary provider fails.
- Existing API endpoints should remain unchanged.
- The frontend should not know which provider generated the response.
- Both providers should expose the same contract.

---

# Architecture Discussion

## Decision Needed

Where should provider selection and fallback logic live?

---

## My Initial Thoughts

Initially I considered changing multiple layers to support Groq streaming.

After analysing responsibilities, I realized only the orchestration layer should know about provider selection.

---

# Final Decision

Responsibilities were divided as follows:

- Provider services communicate with their respective SDKs.
- `service.py` owns provider routing and fallback.
- `conversation_service.py` owns the conversation workflow.
- `main.py` remains responsible only for HTTP.

---

# Implementation Summary

Completed:

- Refactored Groq to the native Chat Completions API.
- Implemented Groq streaming.
- Added Gemini → Groq streaming fallback.
- Verified the streaming contract remained unchanged.
- Verified the conversation workflow required no changes.

---

# Architecture Validation

One of the strongest indicators that the architecture was correct was that introducing a second provider required changes only inside:

- `groq_service.py`
- `service.py`

No changes were required in:

- `main.py`
- `conversation_service.py`

This confirmed that responsibilities had been separated correctly.

---

# Lessons Learned

- Stable contracts reduce future development effort.
- Good architecture minimizes the number of files that change.
- Provider implementations should hide SDK-specific details.
- Responsibilities should be identified before implementation begins.

---

# Sprint Backlog

## Story 1

Title: Native Groq Integration

Status: Completed

---

## Story 2

Title: Groq Streaming

Status: Completed

---

## Story 3

Title: Streaming Provider Fallback

Status: Completed

---

## Story 4

Title: Validate Provider Contract

Status: Completed

---

# Sprint Summary

## Completed

- Native Groq SDK integration.
- Groq Chat Completions.
- Groq Streaming.
- Streaming fallback.
- End-to-end provider validation.

---

## Future Improvements

- Structured logging.
- Retry policies.
- Additional provider support.
- Provider health monitoring.