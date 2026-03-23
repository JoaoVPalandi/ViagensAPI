from pydantic import BaseModel
from typing import Optional

class MetodoPagamentoSchema(BaseModel):
    descricao: Optional[str] = None
    nome_financeira: Optional[str] = None

    class Config:
        from_attributes = True