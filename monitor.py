import psutil
import time
import logging
import os

# Cria a pasta de logs se ela não existir dentro do container
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configura o logging para escrever no terminal E no arquivo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/monitoramento.log"), # Salva no arquivo
        logging.StreamHandler()                        # Mostra no terminal
    ]
)

LIMIT_CPU = 80.0

def monitorar():
    while True:
        cpu_uso = psutil.cpu_percent(interval=1)
        if cpu_uso > LIMIT_CPU:
            logging.error(f"ALERTA: Uso crítico de CPU: {cpu_uso}%")
        else:
            logging.info(f"Sistema normal - CPU: {cpu_uso}%")
        time.sleep(5)

if __name__ == "__main__":
    logging.info("Iniciando monitoramento com persistência de logs...")
    monitorar()