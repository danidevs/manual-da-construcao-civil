#!/usr/bin/env python
# src/manual_da_construcao_civil/main.py

import sys
import warnings
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importação da classe da Crew atualizada com a marca COPE
from cope.crew import CopeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# =====================================================================
# CONFIGURAÇÃO DA API PARA O APLICATIVO DE CELULAR (MOBILE)
# =====================================================================

app = FastAPI(
    title="COPE - Colher de Pedreiro Executiva API",
    description="Motor de inteligência multiagente assíncrono para suporte técnico e logístico em canteiros de obras.",
    version="1.0.0"
)

# Modelo de dados recebido do aplicativo móvel via requisição JSON
class PerguntaInput(BaseModel):
    pergunta_usuario: str

@app.post("/api/perguntar")
def api_perguntar_agente(input_data: PerguntaInput):
    try:
        # Instancia a Crew orquestrada pelo COPE
        crew_instancia = CopeCrew().crew()
        
        # Mapeia a dúvida do campo vinda do celular para o input das tarefas da equipe
        inputs = {
            'tema': input_data.pergunta_usuario
        }
        
        # Executa a linha de raciocínio sequencial dos agentes especialistas
        resultado = crew_instancia.kickoff(inputs=inputs)
        
        # Retorna o relatório final consolidado estruturado para a tela do app
        return {"resposta": str(resultado)}
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Falha na execução interna dos agentes COPE: {str(e)}"
        )


# =====================================================================
# COMANDOS DA CLI DO CREWAI (VERSIONAMENTO E EXECUÇÃO LOCAL PELO TERMINAL)
# =====================================================================

def run():
    """
    Executa a tripulação localmente via comando terminal: crewai run
    """
    inputs = {
        'tema': 'Construção de Casa Residencial de Médio Padrão'
    }
    CopeCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Treina a tripulação para otimizar os prompts ao longo de iterações: crewai train <iterações> <arquivo>
    """
    inputs = {
        'tema': 'Construção de Casa Residencial de Médio Padrão'
    }
    try:
        CopeCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Erro durante a rotina de treinamento da Crew: {e}")

def replay():
    """
    Repete a execução da tripulação a partir de uma tarefa específica: crewai replay <task_id>
    """
    try:
        CopeCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Erro ao tentar reexecutar a tarefa selecionada: {e}")

def test():
    """
    Testa o pipeline e retorna métricas de desempenho: crewai test <iterações> <modelo>
    """
    inputs = {
        'tema': 'Construção de Casa Residencial de Médio Padrão'
    }
    try:
        CopeCrew().crew().test(n_iterations=int(sys.argv[1]), model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Erro durante a validação de testes do motor de IA: {e}")
