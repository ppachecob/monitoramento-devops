import sqlite3
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# --- 1. CONFIGURAÇÃO ---
load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def consultar_media_e_enviar():
    # Conecta ao banco para buscar os dados
    conexao = sqlite3.connect('meu_projeto.db')
    cursor = conexao.cursor()
    
    # Busca os preços e a quantidade de registros
    cursor.execute("SELECT preco FROM historico_precos")
    precos = cursor.fetchall() # Retorna uma lista de tuplas [(50000.0,), (51000.0,)]
    
    if not precos:
        print("Banco de dados vazio.")
        return

    # Lógica de cálculo
    total_registros = len(precos)
    soma = sum(p[0] for p in precos)
    media = soma / total_registros
    ultimo_preco = precos[-1][0] # Pega o último preço inserido

    conexao.close()

    # --- 2. PREPARANDO A MENSAGEM PARA O DISCORD ---
    # Usamos f-strings para formatar o texto de forma profissional
    mensagem = {
        "content": f"📊 **Relatório de Monitoramento DevOps**\n"
                   f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
                   f"📈 Última Cotação: ${ultimo_preco:,.2f}\n"
                   f"🧮 Média das Cotações: **${media:,.2f}**\n"
                   f"📂 Registros no Banco: {total_registros}\n"
                   f"✅ Sistema Operante."
    }

    # --- 3. ENVIO VIA API (A LIGAÇÃO FINAL) ---
    try:
        resposta = requests.post(WEBHOOK_URL, json=mensagem)
        if resposta.status_code == 204:
            print("Relatório enviado com sucesso para o Discord!")
        else:
            print(f"Erro ao enviar: {resposta.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

if __name__ == "__main__":
    consultar_media_e_enviar()