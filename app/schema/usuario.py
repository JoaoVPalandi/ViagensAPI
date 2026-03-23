from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    idade: Optional[int] = None
    data_nascimento: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    username: Optional[str] = None

    class Config:
        from_attributes = True