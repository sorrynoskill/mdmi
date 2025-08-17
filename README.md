# MDMI Starter (FastAPI + Next.js + PostgreSQL + Redis)

Un schelet minim pentru proiectul tău **MDMI** (Multi‑Dimensional Market Insight).

## Ce include
- **backend/** – FastAPI + pytest, structură pregătită pentru PG + Redis
- **frontend/** – Next.js (TypeScript) cu pagină de start
- **docker-compose.yml** – Postgres + Redis (opțional, pentru local/dev)
- **setup.sh** – folosit de Codex pentru a instala dependențele backend
- **AGENTS.md** – taskuri clare pentru Codex (feature-uri MDMI)
- **CI** – workflow simplu GitHub Actions pentru teste Python

> Notă: În Codex, de obicei rulezi backend-ul și testele. Frontend-ul e inclus ca schelet (poate fi extins de Codex într-un PR).

## Quick start local (opțional)
```bash
# Backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000

# Test suite
pytest -q

# Dev services (DB + cache)
docker compose up -d db redis
```

## Endpointuri inițiale
- `GET /health` – status
- `GET /config` – config minimă pentru verificare
