import os
import psutil
import requests
import time
import json
from dotenv import load_dotenv

# Carrega as configurações do cofre
load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def coletar_metricas():
    # Coleta os dados do hardware do seu i7
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    return cpu, ram, disco

def avaliar_e_notificar():
    cpu, ram, disco = coletar_metricas()
    max_uso = max(cpu, ram, disco) # Encontra o recurso mais carregado

    # Lógica de Alerta
    if max_uso > 80:
        status = "🔴 CRÍTICO"
        cor = 16711680 # Vermelho em decimal
    elif max_uso > 60:
        status = "⚠️ ATENÇÃO"
        cor = 16776960 # Amarelo em decimal
    else:
        return # Se estiver tudo OK, não envia nada para não poluir o Discord

    # Montando a carga (Payload) para o Discord
    payload = {
        "embeds": [{
            "title": f"Monitoramento: {status}",
            "description": f"O recurso mais alto atingiu {max_uso}%",
            "color": cor,
            "fields": [
                {"name": "CPU", "value": f"{cpu}%", "inline": True},
                {"name": "RAM", "value": f"{ram}%", "inline": True},
                {"name": "Disco", "value": f"{disco}%", "inline": True}
            ]
        }]
    }

    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json=payload)
        print(f"Alerta enviado: {status}")

# No início do seu script, fora do loop
contagem_critica = 0
LIMITE_PERSISTENCIA = 3 # Precisa falhar 3 vezes seguidas (3 minutos)

# No seu loop principal, logo após coletar as métricas:
if __name__ == "__main__":
    print("🚀 Monitoramento inteligente iniciado...", flush=True)
    try:
        while True:
            cpu, ram, disco = coletar_metricas()
            max_uso = max(cpu, ram, disco)

            # --- ADICIONE ESTA LINHA ABAIXO ---
            print(f"I'm alive! [CPU: {cpu}% | RAM: {ram}% | Disk: {disco}%]", flush=True)
            # ---------------------------------

            if max_uso > 80:
                contagem_critica += 1
                print(f"⚠️ Uso alto detectado: {max_uso}% ({contagem_critica}/{LIMITE_PERSISTENCIA})")
                
                # Só dispara o alerta se atingir o limite
                if contagem_critica >= LIMITE_PERSISTENCIA:
                    avaliar_e_notificar() # Sua função de envio
                    contagem_critica = 0 # Reset após o alerta
            else:
                if contagem_critica > 0:
                    print("✅ Uso normalizado. Contador resetado.")
                contagem_critica = 0 # Reseta o contador se o uso baixar

            time.sleep(60) # Intervalo de 1 minuto
    except KeyboardInterrupt:
        print("\n🛑 Encerrado.")