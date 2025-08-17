# AGENTS.md – brief pentru Codex

## Context
Proiect **MDMI**: platformă de analiză multi‑dimensională pentru piețe (indicatori tehnici, sentiment, management risc, execuție).

## Backlog inițial (te rog fă PR-uri mici și testate)
1. **DB models + alembic**: configurează SQLAlchemy pentru PostgreSQL. Tabele: `symbols`, `signals`, `trades`, `optimizations`. Creează migrații.
2. **Redis caching**: wrapper simplu pentru stocare temporară a semnalelor și ratelimiting.
3. **Indicatori**: implementă calcul EMA(9/21) și RSI(14) în `backend/app/indicators/ta.py` cu teste.
4. **Strategie**: un `scalping.py` care folosește EMA/RSI și livrează semnale buy/sell + backtest simplu.
5. **WebSockets**: endpoint `/ws/stream` care transmite semnale în timp real (mock la început).
6. **Binance Spot (paper/sandbox)**: serviciu care trimite ordine în modul paper + log în DB. Cheile din env.
7. **Discord notifications**: webhook pentru alerte (nu Telegram).
8. **Frontend wiring**: pagină Next.js care consumă `/health`, afișează semnale live prin WS și un mic dashboard.
9. **Config & Secrets**: `.env`, validare cu pydantic-settings. Nu comita chei reale.
10. **CI**: rulează teste + linters. Adaugă matrix Python 3.10/3.11.

## Instrucțiuni de rulare în Codex
- Execută `setup.sh` (instalează dependențe backend). Internetul e folosit doar în timpul setup-ului.
- Rulează testele: `pytest -q`.
- Orice cod nou trebuie acoperit de teste și tipat (mypy în pasul următor).
