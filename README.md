# 💰 Controle Financeiro

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge\&logo=react\&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge\&logo=vite\&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge\&logo=tailwind-css\&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge\&logo=sqlalchemy\&logoColor=white)

Sistema Full Stack para gerenciamento de finanças pessoais desenvolvido utilizando **FastAPI** e **React**.

O projeto permite o gerenciamento de usuários, categorias e transações financeiras através de uma API REST documentada automaticamente, seguindo arquitetura em camadas e boas práticas de desenvolvimento backend.

---

# 📸 Demonstração

> *(Adicionar screenshots da aplicação aqui)*

* Login
* Dashboard
* Cadastro de Transações
* Cadastro de Categorias

---

# ✨ Funcionalidades

### 👤 Usuários

* Cadastro de usuários
* Login
* Validação de dados
* Armazenamento seguro de senhas

### 💰 Transações

* Cadastro de receitas
* Cadastro de despesas
* Atualização de transações
* Exclusão de transações
* Consulta de movimentações

### 📂 Categorias

* Cadastro de categorias
* Atualização
* Exclusão
* Associação com transações

### 🌐 API REST

* Endpoints organizados
* Validação automática de requisições
* Documentação Swagger
* Separação entre camadas da aplicação

---

# 🛠️ Tecnologias

| Categoria      | Tecnologia   |
| -------------- | ------------ |
| Backend        | FastAPI      |
| Frontend       | React        |
| Build          | Vite         |
| ORM            | SQLAlchemy   |
| Banco de Dados | SQLite       |
| Validação      | Pydantic     |
| Estilização    | Tailwind CSS |

---

# 🏗️ Arquitetura

O backend foi desenvolvido utilizando arquitetura em camadas, separando claramente as responsabilidades da aplicação.

```text
Cliente (React)

        │

        ▼

FastAPI (Routers)

        │

        ▼

Services

        │

        ▼

Repositories

        │

        ▼

SQLite
```

Essa abordagem facilita a manutenção, reutilização de código e evolução do sistema.

---

# 📂 Estrutura do Projeto

```text
controle-financeiro/

├── backend/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── App.jsx
│
└── README.md
```

---

# 🚀 Como executar

## Clonando o projeto

```bash
git clone https://github.com/JacksonPandolfo/controle-financeiro.git

cd controle-financeiro
```

## Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Aplicação:

```
http://localhost:5173
```

---

# 🔒 Boas práticas adotadas

* Arquitetura em camadas
* Repository Pattern
* Service Layer
* Separação de responsabilidades
* Validação de dados com Pydantic
* Variáveis de ambiente (.env)
* Hash de senhas
* Organização em monorepositório

---

# 🚧 Próximas melhorias

* Autenticação JWT
* Dashboard com gráficos
* Relatórios financeiros
* Filtros por período
* Docker
* Testes automatizados
* Deploy em nuvem

---

# 👨‍💻 Autor

**Jackson Pandolfo**

Graduado em Análise e Desenvolvimento de Sistemas e pós-graduando em Inteligência Artificial Aplicada.

Desenvolvedor focado em Backend utilizando Python, FastAPI e bancos de dados relacionais.

LinkedIn: www.linkedin.com/in/jacksonpandolfo

