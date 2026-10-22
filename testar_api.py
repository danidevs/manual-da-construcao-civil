# src/manual_da_construcao_civil/test_api_client.py

import requests
# Caso faça importação do main ou da crew
from cope.main import app

# Endereço local padrão (Ajuste a porta caso seu backend use outra, ex: 8000 para FastAPI)
PORTA_API = "8000"
URL = f"http://127.0.0.1:{PORTA_API}/api/v1/run"  # Rota fictícia comum de execução

# Payload de dados configurado para o ecossistema COPE
dados = {
    "pergunta_usuario": "Quais são os principais cuidados na concretagem de uma fundação?"
}

print("======================================================================")
print("🛠️  COPE - TESTE DE INTEGRAÇÃO API")
print(f"Conectando ao Motor de IA do COPE em: {URL}...")
print("======================================================================")

try:
    # Realiza a chamada post enviando o arquivo JSON
    resposta = requests.post(URL, json=dados, timeout=120)  # Timeout estendido para dar tempo à LLM local
    
    if resposta.status_code == 200:
        print("\n🤖 [SISTEMA COPE] RETORNO DA TRIPULAÇÃO COM SUCESSO:\n")
        # Captura a resposta estruturada vinda do motor de IA
        resultado_ia = resposta.json().get("resposta", "Nenhum retorno gerado.")
        print(resultado_ia)
    else:
        print(f"\n❌ Erro de comunicação com o COPE: Código HTTP {resposta.status_code}")
        print(f"Detalhes do erro: {resposta.text}")
        
except requests.exceptions.Timeout:
    print("\n❌ Tempo limite esgotado! O motor do COPE (Llama 3.1 local) demorou mais que o esperado para responder.")
except requests.exceptions.ConnectionError:
    print(f"\n❌ Falha de Conexão! Certifique-se de que o servidor do COPE está rodando na porta {PORTA_API}.")
except Exception as e:
    print(f"\n❌ Ocorreu um erro inesperado ao tentar acionar o COPE: {e}")

print("\n======================================================================")
