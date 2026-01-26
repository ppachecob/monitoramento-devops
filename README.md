# 🚀 System Monitor: Real-time Resources to Discord

Este projeto consiste em um agente de monitoramento resiliente, desenvolvido em **Python**, que monitora métricas críticas de hardware (CPU, RAM e Disco) e envia alertas inteligentes para um canal do **Discord** via Webhooks.

O sistema foi projetado com foco em princípios de **DevOps**, utilizando conteinerização e boas práticas de segurança.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**: Lógica do monitor e coleta de métricas (`psutil`).
* **Docker & Docker Compose V2**: Orquestração e isolamento do ambiente.
* **Discord Webhooks**: Interface de saída para alertas em tempo real.
* **Dotenv (.env)**: Gestão segura de variáveis de ambiente.

## 🏗️ Arquitetura do Sistema

O diagrama abaixo ilustra o fluxo de dados desde a coleta no host até a notificação final:



1.  **Host (Ubuntu Server)**: Onde o monitor extrai os dados brutos de hardware.
2.  **Container Docker**: Isola a aplicação, garantindo que ela rode em qualquer servidor.
3.  **Segurança**: A URL do Webhook nunca é exposta no código, sendo carregada via arquivo `.env`.
4.  **Lógica de Severidade**:
    * **Uso < 80%**: Silencioso (estável).
    * **Uso >= 80%**: Alerta de Atenção (Amarelo).
    * **Uso >= 95%**: Alerta Crítico (Vermelho).

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/ppachecob/monitoramento-devops.git](https://github.com/ppachecob/monitoramento-devops.git)

## 🤖 Automação e CI/CD Local

Para otimizar o fluxo de trabalho, foi implementado um pipeline de automação (`automate_all.sh`) que realiza:
1. **Sincronização**: Pull das últimas atualizações do repositório remoto.
2. **Deploy**: Build e reinicialização dos containers via Docker Compose V2.
3. **Backup**: Commit e Push automático do estado atual para o GitHub.

Este script garante a integridade do ambiente e a persistência das métricas monitoradas.