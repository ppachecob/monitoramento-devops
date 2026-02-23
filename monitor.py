import os
import psutil
import requests
import time
import json
from dotenv import load_dotenv


# Força o carregamento das variáveis de ambiente
load_dotenv()
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def enviar_alerta_completo(ram, cpu, disco):
    # Calcula o maior uso para definir a gravidade
    max_uso = max(ram, cpu, disco)
    
    # Cores em Decimal: Vermelho (Crítico) ou Amarelo (Atenção)
    cor = 15158332 if max_uso >= 95 else 16776960
    titulo = "🔴 ALERTA CRÍTICO" if max_uso >= 95 else "⚠️ ATENÇÃO: USO ELEVADO"

    payload = {
        "embeds": [{
            "title": titulo,
            "color": cor,
            "fields": [
                {"name": "🧠 RAM", "value": f"{ram}%", "inline": True},
                {"name": "⚡ CPU", "value": f"{cpu}%", "inline": True},
                {"name": "💽 Disco", "value": f"{disco}%", "inline": True}
            ],
            "footer": {"text": "Monitoramento Integrado - Ubuntu Server"},
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
        }]
    }
    
    try:
        # Envia a requisição e armazena a resposta
        r = requests.post(WEBHOOK_URL, json=payload)
        # O flush=True garante que o log apareça na hora no Docker
        print(f"📡 Status Discord: {r.status_code} | Maior Uso: {max_uso}%", flush=True)
    except Exception as e:
        print(f"🚨 Erro ao enviar para o Discord: {e}", flush=True)

print("🚀 Monitoramento de Recursos (RAM, CPU, Disco) Iniciado...", flush=True)

while True:
    # Coleta de métricas
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1) # O intervalo de 1s é ideal para precisão
    disco = psutil.disk_usage('/').percent
    
    # Lógica de disparo
    if max(ram, cpu, disco) >= 80:
        enviar_alerta_completo(ram, cpu, disco)
    
    # Aguarda 60 segundos para a próxima verificação
    time.sleep(60)
