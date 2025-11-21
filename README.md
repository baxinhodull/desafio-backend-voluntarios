# API de Gerenciamento de Voluntários 🤝

API REST desenvolvida com **FastAPI** e gerenciada via **Poetry** para o cadastro e controle de voluntários.

## 🚀 Tecnologias
- Python 3.13+
- FastAPI
- Pydantic
- Poetry (Gerenciamento de dependências)
- Pytest (Testes automatizados)

## ⚙️ Como Executar

### Pré-requisitos
Certifique-se de ter o [Poetry](https://python-poetry.org/docs/) instalado.

1. **Instale as dependências:**
   bash
   poetry install


2. **Execute o servidor:**
   poetry run uvicorn main:app --reload


3. **Acesse a documentação interativa:**
   Swagger UI: http://127.0.0.1:8000/docs

   ReDoc: http://127.0.0.1:8000/redoc

4. **🧪 Como Testar**
O projeto inclui testes automatizados para garantir a integridade dos dados.
poetry run pytest


| Método | Rota                | Descrição                                               |
| ------ | ------------------- | ------------------------------------------------------- |
| POST   | `/voluntarios`      | Cadastra um novo voluntário (validação de e-mail único) |
| GET    | `/voluntarios`      | Lista voluntários (filtros por cargo e disponibilidade) |
| GET    | `/voluntarios/{id}` | Obtém detalhes de um voluntário específico              |
| PUT    | `/voluntarios/{id}` | Atualiza os dados de um voluntário                      |
| DELETE | `/voluntarios/{id}` | Remove um voluntário (soft delete)                      |
