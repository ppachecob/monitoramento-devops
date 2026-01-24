#!/bin/bash

echo "🚀 Iniciando Deploy com Docker Compose V2..."

# 1. Garante que não existam fantasmas (Down com remove orphans)
docker compose down --remove-orphans

# 2. Builda e sobe os containers
docker compose up -d --build

# 3. Limpa imagens que não estão sendo usadas (DevOps clean)
docker image prune -f

echo "✅ Deploy finalizado com sucesso!"