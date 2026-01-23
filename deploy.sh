#!/bin/bash
set -e  # Para o script se houver qualquer erro
# ... resto do script

echo "🚀 Iniciando atualização do sistema de monitoramento..."

# 1. Puxa as últimas mudanças do GitHub
git pull origin main

# No seu deploy.sh, altere a linha do docker-compose para:
docker-compose up -d --build --remove-orphans

# 3. Limpa imagens antigas que não estão sendo usadas (manter o servidor limpo)
docker image prune -f

echo "✅ Sistema atualizado e rodando!"