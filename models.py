from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional


class Disponibilidade(str, Enum):
    MANHA = "manha"
    TARDE = "tarde"
    NOITE = "noite"

class Volunteer(BaseModel):
    id: int
    name: str
    email: EmailStr
    telefone: str
    cargo_pretendido: str
    disponibilidade: Disponibilidade
    active: bool = True
    created_at: datetime = datetime.now()