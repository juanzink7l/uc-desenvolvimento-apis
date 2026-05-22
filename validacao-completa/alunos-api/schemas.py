from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description='Nome completo do aluno')
    email: EmailStr = Field(..., description='E-mail válido')
    matricula: int = Field(..., description='Número de matrícula')
    nota_final: Optional[float] = Field(None, ge=0, le=10, description='Nota final entre 0 e 10')
    @field_validator('matricula')
    @classmethod

    def matricula_valida(cls, v: str) -> str:
        if v <= 0:
            raise ValueError('Matricula deve conter apenas numeros')
        return v

class AlunoPatch(BaseModel):
    nota_final: Optional[float] = Field(None, ge=0, le=10)
    email: Optional[EmailStr] = None
    nome: Optional[str] = None

    @field_validator('nome')
    @classmethod
    def nome_sem_numero(cls, v):
        if v and any(char.isdigit() for char in v):
            raise ValueError('O nome nao pode conter numeros')
        return v.strip() if v else v

class AlunoResponse(BaseModel):
    id: int
    nome: str
    email: str
    matricula: int
    nota_final: int
    ativo: bool
    criado_em: datetime
    
    class Config:
        from_attributes = True

class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None
