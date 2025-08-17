#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv || python -m venv .venv
source .venv/bin/activate || true

pip install --upgrade pip
pip install -r backend/requirements.txt

echo "Setup complete for backend."
