#!/bin/bash

# --- Configurações ---
PROJECT_DIR="~/monitor/one_project"
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

echo "------------------------------------------"
echo "🚀 [START] Full Automation Pipeline - $TIMESTAMP"
echo "------------------------------------------"

# 1. Sincronização com o GitHub (Entrada)
echo "📥 1/3: Fetching latest changes from GitHub..."
git pull origin main

# 2. Deploy com Docker Compose V2 (Operação)
echo "🐳 2/3: Rebuilding and Starting Containers..."
docker compose down --remove-orphans
docker compose up -d --build

# 3. Registro e Backup (Saída)
echo "📤 3/3: Saving local progress to GitHub..."
git add .
git commit -m "Auto-deploy & documentation update: $TIMESTAMP"
git push origin main

echo "------------------------------------------"
echo "✅ [SUCCESS] Environment is Up and Synced!"
echo "------------------------------------------"
