from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class AlunoCadastrado(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description='Nome completo do aluno')
    email: EmailStr = Field(..., description='E-mail válido')
    matricula: str = Field(..., min_length=8, max_length=8, description='Número de matrícula')
    nota_final: Optional[float] = Field(None, ge=0, le=10, description='Nota final entre 0 e 10')
    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, v: str) -> str:
        if any(char.isdigit() for char in v):
            raise ValueError('Nome nao pode conter numeros')
        if not v.strip():
            raise ValueError('Nome nao pode ser só espaços')
        return v.strip()

    def matricula_valida(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError('Matricula deve conter apenas numeros')
        return v

    def nota_final_valida(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and (v < 0 or v > 10):
            raise ValueError('Nota final deve ser entre 0 e 10')
        return v

class AlunoPatch(BaseModel):
    nota_final: Optional[int] = Field(None, min_length=0, max_length=10)
    email: Optional[EmailStr] = None














