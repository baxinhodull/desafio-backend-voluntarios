from pydantic import BaseModel, EmailStr
from models import Disponibilidade

class VolunteerCreate(BaseModel):
    name: str
    email: EmailStr
    telefone: str
    cargo_pretendido: str
    disponibilidade: Disponibilidade