# 5-7 Minute Evaluator Walkthrough

## Opening
“I chose the Team Directory prompt and implemented it as a Capability Team Directory. I wanted to keep the scope small while showing a realistic internal enterprise use case.”

## What the user can do
“The user can search across people, skills, teams, and capabilities. They can also filter by team, role, or skill and open a person to see a small hierarchical capability view with maturity levels.”

## Frontend decisions
“The frontend is React with TypeScript. I kept data types explicit, separated filtering logic from rendering, and added loading, fallback, empty, and responsive states.”

## Backend decisions
“I added a small FastAPI backend because the role includes Python and API-fed content. The API exposes people and metadata endpoints and adds request ID/timing logging.”

## Tradeoffs
“I intentionally did not add a database, authentication, Docker, or deployment automation because the exercise asks us not to overbuild.”

## If I had another day
“I would add server-side pagination, React Query, URL-synchronized filters, Playwright, accessibility validation, Web Vitals, and a richer capability graph.”

## Likely questions
**Why FastAPI?** Lightweight, typed through Pydantic, and a good fit for Python API development.

**Why no database?** Persistence would add setup cost without improving the main demonstration within the time limit.

**How would you scale it?** Move filtering/pagination server-side, persist data, add caching, and index searchable fields.

**How would you add real-time updates?** Add WebSocket/STOMP events and reconcile updates into client state.

**How would you add AI?** Add a knowledge endpoint that answers capability ownership questions using retrieved directory context while keeping deterministic search as the source of truth.
