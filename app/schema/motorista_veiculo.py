from pydantic import BaseModel
from typing import Optional

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: Optional[int] = None
    id_veiculo: Optional[int] = None
    datahora_inicio: str
    datahora_fim: str

    class Config:
        from_attributes = True