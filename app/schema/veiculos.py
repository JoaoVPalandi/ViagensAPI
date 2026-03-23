from pydantic import BaseModel
from typing import Optional

class VeiculoSchema(BaseModel):
    placa: Optional[str] = None
    tem_seguro: Optional[str] = None
    id_modelo_veiculo: Optional[int] = None
    id_classe_veiculo: Optional[int] = None

    class Config:
        from_attributes = True

