# src/manual_da_construcao_civil/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CopeCrew():
    """Crew responsável pela orquestração do ecossistema COPE (Colher de Pedreiro Executiva)"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- AGENTES (Especialistas COPE) ---

    @agent
    def arquiteto(self) -> Agent:
        return Agent(
            config=self.agents_config['arquiteto'],
            verbose=True
        )

    @agent
    def engenheiro_civil(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_civil'],
            verbose=True
        )

    @agent
    def engenheiro_eletrico(self) -> Agent:
        return Agent(
            config=self.agents_config['engenheiro_eletrico'],
            verbose=True
        )

    @agent
    def mestre_de_obras(self) -> Agent:
        return Agent(
            config=self.agents_config['mestre_de_obras'],
            verbose=True
        )

    @agent
    def pedreiro_alvenaria(self) -> Agent:
        return Agent(
            config=self.agents_config['pedreiro_alvenaria'],
            verbose=True
        )

    @agent
    def pedreiro_acabamento(self) -> Agent:
        return Agent(
            config=self.agents_config['pedreiro_acabamento'],
            verbose=True
        )

    @agent
    def pintor(self) -> Agent:
        return Agent(
            config=self.agents_config['pintor'],
            verbose=True
        )

    # --- TAREFAS (Fluxo Construtivo COPE) ---

    @task
    def tarefa_arquitetura(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_arquitetura']
        )

    @task
    def tarefa_estrutura_civil(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_estrutura_civil']
        )

    @task
    def tarefa_instalacao_eletrica(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_instalacao_eletrica']
        )

    @task
    def tarefa_planejamento_canteiro(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_planejamento_canteiro']
        )

    @task
    def tarefa_erguer_alvenaria(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_erguer_alvenaria']
        )

    @task
    def tarefa_aplicar_acabamento(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_aplicar_acabamento']
        )

    @task
    def tarefa_pintura_final(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_pintura_final']
        )

    # --- COORDENAÇÃO DA TRIPULAÇÃO ---

    @crew
    def crew(self) -> Crew:
        """Cria e injeta o fluxo de execução sequencial do COPE"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True, # <-- Garante que cada pensamento apareça no terminal na hora
            memory=False  # <-- Desative a memória temporariamente para poupar processamento local
        )

