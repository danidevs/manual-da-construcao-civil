import requests

# URL totalmente corrigida com o IP e a porta certa
URL = "http://127.0.0"

dados = {
    "pergunta_usuario": "Quais sao os principais cuidados na concretagem de uma fundacao?"
}

print("Chamando o agente do CrewAI via API... Aguarde alguns segundos...")

try:
    resposta = requests.post(URL, json=dados)
    if resposta.status_code == 200:
        print("\n🤖 RESPOSTA DO AGENTE:\n")
        print(resposta.json()["resposta"])
    else:
        print(f"\n❌ Erro na API: Codigo {resposta.status_code}")
        print(resposta.text)
except Exception as e:
    print(f"\n❌ Nao foi possivel conectar na API. Erro: {e}")
