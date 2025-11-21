from fastapi.testclient import TestClient
from main import app
from crud import db  # <--- AGORA SIM: Importando do crud.py

client = TestClient(app)

def setup_function():
    # Limpa o banco antes de cada teste
    db.clear()
    # Reseta o ID
    import crud
    crud.current_id = 1

def test_criar_voluntario_valido():
    payload = {
        "name": "Tester Silva",
        "email": "teste@exemplo.com",
        "telefone": "11999999999",
        "cargo_pretendido": "Analista de Dados",
        "disponibilidade": "manha"
    }
    response = client.post("/voluntarios", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "teste@exemplo.com"

def test_nao_permitir_email_duplicado():
    payload = {
        "name": "Tester Duplicado",
        "email": "duplicado@exemplo.com",
        "telefone": "11999999999",
        "cargo_pretendido": "QA",
        "disponibilidade": "tarde"
    }
    # Cria o primeiro
    client.post("/voluntarios", json=payload)
    
    # Tenta criar o segundo igual
    response = client.post("/voluntarios", json=payload)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Email já registado."