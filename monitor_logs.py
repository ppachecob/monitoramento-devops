import time
import requests
import os
from dotenv import load_dotenv

# Configurações
load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
LOG_FILE = "/var/log/syslog"

def send_to_discord(message):
    data = {"content": f"🚨 **Alerta de Sistema (UbuntuServer):**\n```{message}```"}
    requests.post(WEBHOOK_URL, json=data)

def monitor_logs():
    # Vai para o fim do arquivo para não ler tudo o que já passou
    stat_info = os.stat(LOG_FILE)
    file_size = stat_info.st_size
    
    with open(LOG_FILE, "r") as f:
        f.seek(file_size)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1) # Espera nova linha
                continue
            
            # Filtros baseados nos seus erros reais
            if "apparmor=\"DENIED\"" in line or "self-detected stall" in line:
                send_to_discord(line.strip())

if __name__ == "__main__":
    print("Monitoramento iniciado...")
    monitor_logs()