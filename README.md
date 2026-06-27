# 💰 Controle Financeiro - Full Stack Monorepo

![Python](https://shields.io)
![FastAPI](https://shields.io)
![Vite](https://shields.io)
![React](https://shields.io)
![Tailwind CSS](https://shields.io)

Este é um sistema de gestão de finanças pessoais desenvolvido originalmente como projeto final para a cadeira de **Fundamentos de Python**. A aplicação foi projetada seguindo rigorosos padrões de arquitetura de software de mercado, contando com uma API RESTful de alta performance no backend e uma interface rica e responsiva no frontend.

---

## 🛠️ Tecnologias e Arquitetura Avançada

### Backend (API)
* **FastAPI & Uvicorn**: Framework assíncrono moderno focado em alta performance e documentação automatizada.
* **SQLAlchemy & SQLite**: Camada de persistência relacional robusta utilizando mapeamento objeto-relacional (ORM).
* **Pydantic (v2)**: Contratos de dados estritos e validação de tipos avançados (como `EmailStr`).
* **Clean Architecture / Pattern Layering**: Separação clara de responsabilidades dividida em:
  * **Routers**: Exposição limpa de endpoints REST.
  * **Services**: Centralização das regras de negócio do sistema.
  * **Repositories**: Isolamento total das consultas e operações diretas de banco de dados (CRUD).
  * **Core**: Centralização de segurança (hashing de senhas), exceções customizadas e injeção de dependências.

### Frontend (Interface)
* **Vite**: Ferramenta de build ultra-rápida para o ecossistema Javascript.
* **Tailwind CSS & PostCSS**: Design modular, utilitário e totalmente responsivo para desktop e mobile.
* **Services Layer**: Isolamento de chamadas HTTP organizadas por domínio da aplicação.

---

## 📂 Estrutura Completa do Monorepo

```text
controle-financeiro/
├── backend/                # Ecossistema do Servidor Python (FastAPI)
│   ├── api/                # Camada de exposição e comunicação externa da API
│   │   └── routers/        # Definição das rotas e endpoints do sistema
│   │       ├── categoria_router.py
│   │       ├── transacao_router.py
│   │       └── usuario_router.py
│   ├── core/               # Configurações globais e utilitários do sistema
│   │   ├── config.py       # Gerenciamento de variáveis de ambiente (.env)
│   │   ├── dependencies.py # Dependências injetáveis (ex: autenticação, get_db)
│   │   ├── enums.py        # Definição de enumeradores e tipos fixos do sistema
│   │   ├── exceptions.py   # Customização e tratamento centralizado de erros
│   │   └── security.py     # Lógica de criptografia de senhas e geração de tokens
│   ├── db/                 # Infraestrutura de persistência de dados
│   │   ├── base.py         # Registro e centralização de tabelas para migrações/criação
│   │   └── session.py      # Configuração do Engine e criação da sessão do SQLAlchemy
│   ├── models/             # Entidades e mapeamento de tabelas do SQLAlchemy
│   │   ├── categoria.py
│   │   ├── transacao.py
│   │   └── usuario.py
│   ├── repositories/       # Camada de acesso ao banco de dados (Consultas, SQL, CRUD bruto)
│   │   ├── categoria_repositorio.py
│   │   ├── transacao_repositorio.py
│   │   └── usuario_repositorio.py
│   ├── schemas/            # Contratos de dados e validações do Pydantic (Request/Response)
│   │   ├── categoria_schema.py
│   │   ├── transacao_schema.py
│   │   └── usuario_schema.py
│   ├── services/           # Camada de regras de negócio e validações da aplicação
│   │   ├── categoria_service.py
│   │   ├── transacao_service.py
│   │   └── usuario_service.py
│   ├── main.py             # Ponto de inicialização do FastAPI e do servidor Uvicorn
│   └── requirements.txt    # Lista oficial de dependências do Python para instalação rápida
├── frontend/               # Interface do Usuário (Vite + React + Tailwind)
│   ├── public/             # Arquivos estáticos (Favicon, manifestos, ativos não processados)
│   ├── src/                # Código-fonte principal da aplicação
│   │   ├── components/     # Componentes visuais reutilizáveis das telas
│   │   │   ├── CategoriaModal.jsx
│   │   │   ├── ConfirmaModal.jsx
│   │   │   └── TransacaoModal.jsx
│   │   ├── icons/          # Elementos visuais e imagens locais do sistema
│   │   │   └── cash_pig.png
│   │   ├── pages/          # Telas completas de rotas da aplicação
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   └── Transacoes.jsx
│   │   ├── services/       # Integração e chamadas de API (Comunicação com o FastAPI)
│   │   │   ├── categoriaApi.jsx
│   │   │   ├── transacaoApi.jsx
│   │   │   └── usuarioApi.jsx
│   │   ├── App.jsx         # Componente raiz que gerencia o fluxo global e rotas
│   │   ├── config.js       # Configurações globais de scripts do frontend
│   │   ├── index.css       # Estilos globais e injeção de diretivas do Tailwind CSS
│   │   └── main.jsx        # Ponto de entrada do React que renderiza a aplicação no DOM
└── README.md           # Apresentação do projeto (Este arquivo)
```
---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonando o Repositório
```bash
git clone https://github.com
cd controle-financeiro
```

### 2. Inicializando o Backend
Navegue até a pasta do servidor e configure o ambiente virtual:
```bash
cd backend
python -m venv venv
```
Ative o ambiente virtual:
* **Windows (PowerShell):** `.\venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

Crie o seu arquivo `.env` na pasta `backend/` seguindo o modelo:
```text
DATABASE_URL=sqlite:///./backend/db/app.db
APP_NAME="Controle Financeiro"
```

Inicie o servidor de desenvolvimento:
```bash
uvicorn main:app --reload
```
A API estará ativa em `http://127.0.0.1:8000`. Acesse a documentação interativaSwagger em `/docs`.

### 3. Inicializando o Frontend
Abra um novo terminal na pasta raiz do projeto e navegue até o frontend:
```bash
cd frontend
```
Instale as dependências do Node:
```bash
npm install
```
Configure o arquivo `.env` do frontend apontando para a API:
```text
VITE_API_URL=http://127.0.0.1:8000
```
Rode o servidor de desenvolvimento do Vite:
```bash
npm run dev
```

---

## 🔒 Segurança e Melhores Práticas Aplicadas
* **Zero Hardcoded Data**: Nenhuma senha, string de conexão de banco de dados ou chave de API foi fixada no código. Tudo é consumido via variáveis de ambiente isoladas.
* **Git Protetor**: Configuração de múltiplos arquivos `.gitignore` para travar uploads de dados confidenciais (`.env`), bancos locais (`app.db`) e pastas pesadas (`node_modules`, `venv`).
