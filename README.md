# 📱 COPE - Colher de Pedreiro Executiva | Mobile App (AI Powered) 🛠️🧠

Este repositório contém o código-fonte do motor de Inteligência Artificial do **COPE (Colher de Pedreiro Executiva)**, um aplicativo de celular desenvolvido para conectar as diretrizes teóricas da Engenharia Civil e Arquitetura diretamente com a realidade prática do canteiro de obras. 

Assim como a tradicional colher de pedreiro molda a massa e assenta o tijolo para dar vida à estrutura, o COPE organiza dados normativos, orçamentos, instalações e fluxos de trabalho em instruções claras, eficientes e acionáveis em tempo real para engenheiros, mestres de obras e construtores.

O projeto faz parte do bootcamp **Bradesco Agentes de IA do Zero à Prática** em parceria com a **DIO**.

---

## 🛠️ Arquitetura do Sistema

O ecossistema combina uma interface mobile ágil com um motor de inteligência artificial descentralizado, focado em autonomia de campo:

- **Frontend Mobile:** Interface otimizada para consultas dinâmicas no chão de fábrica e canteiros.
- **Motor de IA (Orquestração):** Framework **Sub-CrewAI** gerenciando uma equipe multiagente especializada (CopeCrew).
- **Processamento Local (LLM):** Modelo customizado **COPE** rodando 100% local via **Ollama**, garantindo total privacidade de dados, independência de sinal de internet nas obras e custo zero com chaves de API.

---

## 🏗️ Como a IA funciona por trás do App

A inteligência de retaguarda do aplicativo é estruturada através do ecossistema de agentes do COPE e está dividida nos seguintes módulos:

- `src/manual_da_construcao_civil/config/agents.yaml`: Definição de perfis, escopo técnico, *backstory* e estilo de comunicação das personas especializadas (ex: Consultor Financeiro, Arquiteto Sênior, Engenheiro Estrutural, Especialistas em Alvenaria e Acabamentos).
- `src/manual_da_construcao_civil/config/tasks.yaml`: Caderno de encargos técnicos mapeando o fluxo sequencial e condicionado pelo teto financeiro do projeto.
- `src/manual_da_construcao_civil/crew.py`: Arquivo de orquestração estruturado na classe `CopeCrew`, responsável por gerenciar a injeção do modelo local e sincronizar as dependências das tarefas.
- `src/manual_da_construcao_civil/main.py`: Camada de serviço e pontos de entrada que expõem a inteligência dos agentes para consumo da aplicação celular.

---

## 💻 Instalação e Configuração do Motor de IA

Para que o aplicativo possa realizar as consultas de IA de forma offline e local, configure o ambiente de desenvolvimento seguindo as etapas abaixo:

### Pré-requisitos
- Python >= 3.10, < 3.14
- [Ollama](https://ollama.com) instalado e ativo no ambiente local ou servidor de desenvolvimento.
- [UV](https://astral.sh) para gerenciamento de pacotes Python em alta performance.

### 1. Inicializar o Modelo Local Customizado
```bash
ollama run cope
```

### 2. Instalar Dependências do Sistema
Utilizando o gerenciador `uv` na raiz do seu projeto Python:
```bash
pip install uv
crewai install
```

### 3. Variáveis de Ambiente (`.env`)
Certifique-se de que o arquivo `.env` na raiz aponta corretamente para a sua versão customizada do modelo no Ollama:
```env
MODEL=ollama/cope
```

---

## 🚀 Execução e Testes

Seguindo um fluxo profissional rigoroso de engenharia de software (validação de ambiente, execução de pipelines locais e versionamento seguro), você pode disparar a simulação completa da mesa de engenharia do COPE via CLI:

```bash
crewai run
```

---

## 🎯 Status do Roadmap do Projeto
- [x] Modelagem, refinamento e validação do sistema multiagente (**COPE**).
- [x] Inicialização e execução estável homologada localmente via comando `ollama run cope`.
- [x] Versionamento inicial e subida segura no GitHub.
- [ ] Conectar e expor os endpoints de serviço dos agentes para consumo direto na interface do aplicativo mobile.

---
Desenvolvido por Daniel | Portfólio Técnico de IA & Desenvolvimento Mobile.
