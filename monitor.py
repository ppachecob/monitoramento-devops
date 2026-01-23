import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def enviar_alerta_discord(percentual, status="info"):
    # Definindo cores (Decimal): Verde (3066993), Vermelho (15158332)
    cor = 3066993 if status == "ok" else 15158332
    titulo = "✅ Sistema Estável" if status == "ok" else "🚨 Alerta de Uso de Memória"

    payload = {
        "embeds": [{
            "title": titulo,
            "color": cor,
            "fields": [
                {"name": "Servidor", "value": "Ubuntu-Server-PP", "inline": True},
                {"name": "Uso de RAM", "value": f"{percentual}%", "inline": True}
            ],
            "footer": {"text": "Monitoramento Automático - DevOps 2026"}
        }]
    }
    
    requests.post(WEBHOOK_URL, json=payload)

# Exemplo de lógica
uso = 92 # Simulação de uso alto
if uso > 90:
    enviar_alerta_discord(uso, status="critico")