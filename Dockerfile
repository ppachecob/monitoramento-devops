FROM python:3.9-slim

# 1. Define onde os arquivos vão ficar dentro do container
WORKDIR /monitor/one_project

# 2. Copia o arquivo de requisitos PRIMEIRO
COPY requirements.txt .

# 3. Agora sim, instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# 4. Depois copia o seu script
COPY monitor.py .

# 5. Comando para iniciar
CMD ["python", "monitor.py"]

