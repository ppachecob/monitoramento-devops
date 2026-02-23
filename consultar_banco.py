import sqlite3

def consultar_dados():
    # 1. Conecta ao banco de dados existente
    conexao = sqlite3.connect('meu_projeto.db')
    cursor = conexao.cursor()
    
    # 2. Comando SQL para buscar todos os registros
    print("--- Histórico de Preços Salvos ---")
    cursor.execute("SELECT timestamp, preco FROM historico_precos ORDER BY id DESC")
    
    linhas = cursor.fetchall() # Puxa todos os resultados da consulta
    
    soma_precos = 0
    total_registros = len(linhas)

    for linha in linhas:
        data_hora = linha[0]
        valor = linha[1]
        soma_precos += valor
        print(f"Data: {data_hora} | Valor: $ {valor}")

    # 3. Pequena lógica de análise
    if total_registros > 0:
        media = soma_precos / total_registros
        print("-" * 30)
        print(f"Total de registros: {total_registros}")
        print(f"Média dos preços: $ {media:.2f}")
    else:
        print("Nenhum dado encontrado.")

    conexao.close()

if __name__ == "__main__":
    consultar_dados()