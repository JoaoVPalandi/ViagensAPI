from pydantic import BaseModel
from typing import Optional

class MetodoPagamentoSchema(BaseModel):
    descreicao: Optional[str] = None
    metodo_pagamento_id: Optional[int] = None

    class Config:
        from_attributes = True