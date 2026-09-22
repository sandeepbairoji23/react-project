# Capability Team Directory

A small full-stack project built for the **Team Directory** interview prompt.

The app lets users search and browse people across enterprise teams, filter by role and skill, and inspect a lightweight capability hierarchy for each person.

## What I built
- Searchable team directory
- Filters by team, role, and skill
- React + TypeScript UI
- Hierarchical capability display with maturity levels
- Loading, empty, and API fallback states
- Small Python/FastAPI API
- Unit-tested filtering logic
- Request ID and timing logs on the backend

## Why this project
I chose the Team Directory option because it demonstrates data-heavy UI design, search/filtering, hierarchical capability data, API integration, Python data shaping, and maintainable React/TypeScript structure.

## Tech stack
Frontend: React 19, TypeScript, Vite, Vitest
Backend: Python, FastAPI, Pydantic, Uvicorn

## How to run
### Backend
```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:5173

## Assumptions
- Authentication is out of scope.
- Data is mocked/in-memory.
- The backend is intentionally lightweight.
- Maturity is represented as a 1-5 score.

## Intentional tradeoffs
- In-memory data instead of a database to stay within the one-hour spirit.
- No authentication because the exercise is focused on engineering judgment and UX.
- No UI framework so the implementation is easy to review.
- No Docker/CI/CD because the instructions explicitly say not to overbuild.

## If I had another day
1. PostgreSQL persistence
2. Server-side pagination/sorting
3. React Query caching
4. URL-synchronized filters
5. Playwright E2E tests
6. Accessibility audit
7. Web Vitals / RUM
8. Graph visualization
9. SSO/RBAC
10. CI build verification
