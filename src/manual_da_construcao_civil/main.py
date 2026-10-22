#!/usr/bin/env python
import sys
import warnings

# AQUI: Mudamos de ManualDaConstrucaoCivil para ManualDaConstrucaoCivilCrew
from manual_da_construcao_civil.crew import ManualDaConstrucaoCivilCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'tema': 'Construcao de Casa Residencial'
    }
    
    # AQUI TAMBEM: Mudamos o nome da classe que esta sendo chamada
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
