from pydantic import BaseModel
from typing import Optional

class ClasseSchema(BaseModel):
    nome_classe: Optional[str] = None
    fator_preco: Optional[float] = None

    class Config:
        from_attributes = True