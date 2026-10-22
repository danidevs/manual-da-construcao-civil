#!/usr/bin/env python
import sys
import warnings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importação da sua classe de Crew
from manual_da_construcao_civil.crew import ManualDaConstrucaoCivilCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# =====================================================================
# CONFIGURAÇÃO DA API PARA O APLICATIVO DE CELULAR
# =====================================================================

app = FastAPI(title="API do Manual da Construção Civil")

# Modelo de dados que o aplicativo de celular vai enviar no corpo da requisição (JSON)
class PerguntaInput(BaseModel):
    pergunta_usuario: str

@app.post("/api/perguntar")
def api_perguntar_agente(input_data: PerguntaInput):
    try:
        # Instancia a sua Crew
        crew_instancia = ManualDaConstrucaoCivilCrew().crew()
        
        # Mapeia a pergunta vinda do celular para a variável 'tema' esperada pelas suas tasks
        inputs = {
            'tema': input_data.pergunta_usuario
        }
        
        # Executa a inteligência dos agentes
        resultado = crew_instancia.kickoff(inputs=inputs)
        
        # Retorna a resposta final limpa para o front-end do celular
        return {"resposta": str(resultado)}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no agente: {str(e)}")


# =====================================================================
# COMANDOS ORIGINAIS DO CREWAI (MANTIDOS PARA USO NO TERMINAL)
# =====================================================================

def run():
    """
    Run the crew.
    """
    inputs = {
        'tema': 'Construcao de Casa Residencial'
    }
    ManualDaConstrucaoCivilCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'tema': 'Construcao de Casa Residencial'
    }
    try:
        ManualDaConstrucaoCivilCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ManualDaConstrucaoCivilCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'tema': 'Construcao de Casa Residencial'
    }
    try:
        ManualDaConstrucaoCivilCrew().crew().test(n_iterations=int(sys.argv[1]), model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
