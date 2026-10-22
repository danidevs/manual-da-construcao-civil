# 📱 Manual da Construção Civil - Mobile App (AI Powered)

Este repositório contém o código-fonte de um **aplicativo de celular** desenvolvido para levar inteligência artificial diretamente para o canteiro de obras. O objetivo principal é fornecer a engenheiros, arquitetos e mestres de obras um assistente de campo inteligente para consulta de diretrizes de layout, regras de ventilação, incidência solar e boas práticas em tempo real.

O projeto faz parte do bootcamp **Bradesco Agentes de IA do Zero à Prática** em parceria com a **DIO**.

---

## 🛠️ Arquitetura do Sistema

O aplicativo combina uma interface mobile ágil com um motor de inteligência artificial descentralizado e eficiente:

- **Frontend Mobile:** Interface otimizada para o dia a dia no campo de trabalho.
- **Motor de IA (Orquestração):** Framework **CrewAI** gerenciando um sistema multiagente especializado.
- **Processamento Local (LLM):** **Llama 3.1 (8B / 4.9 GB)** rodando 100% local via **Ollama**, garantindo privacidade de dados, autonomia e custo zero com APIs pagas.

---

## 🏗️ Como a IA funciona por trás do App

A inteligência de retaguarda do aplicativo é estruturada através do CrewAI (padrão classic) e está dividida em módulos:

- `src/manual_da_construcao_civil/config/agents.yaml`: Perfil e *backstory* dos agentes especialistas (ex: Engenheiro de Layout, Analista de Conforto Ambiental).
- `src/manual_da_construcao_civil/config/tasks.yaml`: Escopo das análises técnicas de engenharia, ventilação e iluminação natural.
- `src/manual_da_construcao_civil/crew.py`: Configuração do pipeline de IA e injeção do modelo local Llama 3.1.
- `src/manual_da_construcao_civil/main.py`: Camada de serviço que expõe a execução dos agentes para consumo da aplicação celular.

---

## 💻 Instalação e Configuração do Motor de IA

Para que o aplicativo possa realizar as consultas de IA offline/localmente, configure o ambiente de execução:

### Pré-requisitos
- Python >= 3.10, < 3.14
- [Ollama](https://ollama.com) instalado e ativo na máquina local/servidor de desenvolvimento.
- [UV](https://astral.sh) para gerenciamento rápido de pacotes Python.

### 1. Inicializar o Modelo Local
```bash
ollama run llama3.1
```

### 2. Instalar Dependências do Back-end
Utilizando o gerenciador `uv` na raiz do projeto:
```bash
pip install uv
crewai install
```

### 3. Variáveis de Ambiente (`.env`)
Configure o direcionamento para o modelo local:
```env
MODEL=ollama/llama3.1
```

---

## 🚀 Execução e Testes

Seguindo um fluxo profissional rigoroso de engenharia de software (validação de ambiente, execução de testes e commits seguros no GitHub), você pode testar o motor de IA isoladamente via CLI com o comando:

```bash
crewai run
```

---

## 🎯 Status do Roadmap do Projeto
- [x] Modelagem e validação do sistema multiagente (CrewAI).
- [x] Execução estável e homologada com Llama 3.1 local via Ollama.
- [x] Versionamento inicial seguro no GitHub.
- [ ] Conectar e expor os agentes para consumo direto na interface do aplicativo mobile.

---
Desenvolvido por Daniel | Portfólio Técnico de IA & Desenvolvimento Mobile.
