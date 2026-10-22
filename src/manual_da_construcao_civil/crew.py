from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ManualDaConstrucaoCivilCrew():
    """ManualDaConstrucaoCivil crew"""

    # Mantem o padrao do CrewAI de ler os arquivos sem acentos
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- AGENTES ---

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

    # --- TAREFAS ---

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

    # --- COORDENACAO DA CREW ---

    @crew
    def crew(self) -> Crew:
        """Creates the ManualDaConstrucaoCivil crew"""
        return Crew(
            agents=self.agents,  # Automaticamente pega todos os @agent listados acima
            tasks=self.tasks,    # Automaticamente pega todas as @task listadas acima na ordem correta
            process=Process.sequential,  # Linha de producao garantida
            verbose=True,
        )
