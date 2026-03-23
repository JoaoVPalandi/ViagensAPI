from pydantic import BaseModel
from typing import Optional

class ServicoSchema(BaseModel):
    nome_servico: Optional[str] = None
    id_classe_minima: Optional[int] = None

    class Config:
        from_attributes = True
