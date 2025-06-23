#!/bin/bash
cd "$(dirname "$0")/.."
clear
echo "🔧 Iniciando Panel CLI..."

if [ -f "./venv/bin/python" ]; then
  ./venv/bin/python main.py
else
  python3 main.py
fi