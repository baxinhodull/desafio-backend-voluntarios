from models import Volunteer, Disponibilidade
from schemas import VolunteerCreate
from datetime import datetime
from fastapi import HTTPException

# Simulação de banco de dados em memória
db = []
current_id = 1

def create_volunteer(volunteer_in: VolunteerCreate):
    global current_id
    
    # Validação: Verificar se o email já existe e está ativo
    for v in db:
        if v.email == volunteer_in.email and v.active:
            raise HTTPException(status_code=400, detail="Email já registado.")

    # Cria o novo voluntário com os dados recebidos
    new_volunteer = Volunteer(
        id=current_id,
        name=volunteer_in.name,
        email=volunteer_in.email,
        telefone=volunteer_in.telefone,
        cargo_pretendido=volunteer_in.cargo_pretendido,
        disponibilidade=volunteer_in.disponibilidade,
        active=True,
        created_at=datetime.now()
    )
    
    db.append(new_volunteer)
    current_id += 1
    return new_volunteer

def list_volunteers(disponibilidade: str = None, cargo: str = None):
    resultado = []
    for v in db:
        # Apenas voluntários ativos
        if v.active:
            # Filtro de disponibilidade
            if disponibilidade and v.disponibilidade != disponibilidade:
                continue
            # Filtro de cargo
            if cargo and v.cargo_pretendido != cargo:
                continue
            resultado.append(v)
    return resultado

def get_volunteer(vol_id: int):
    for v in db:
        if v.id == vol_id and v.active:
            return v
    return None

def update_volunteer(vol_id: int, volunteer_in: VolunteerCreate):
    for v in db:
        if v.id == vol_id and v.active:
            v.name = volunteer_in.name
            v.email = volunteer_in.email
            v.telefone = volunteer_in.telefone
            v.cargo_pretendido = volunteer_in.cargo_pretendido
            v.disponibilidade = volunteer_in.disponibilidade
            return v
    return None

def delete_volunteer(vol_id: int):
    for v in db:
        if v.id == vol_id and v.active:
            v.active = False  # Soft delete
            return v
    return None