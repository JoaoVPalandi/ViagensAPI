from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AvaliacaoSchema(BaseModel):
    nota_passageiro: Optional[float] = None
    nota_motorista: Optional[float] = None
    datahora_avaliacao: Optional[datetime] = None

    class Config:
        from_attributes = True

