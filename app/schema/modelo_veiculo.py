from pydantic import BaseModel
from typing import Optional

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: Optional[str] = None
    fabricante: Optional[str] = None
    cor: Optional[str] = None
    ano: Optional[int] = None
    capacidade: Optional[int] = None
    propriedade: Optional[str] = None
    id_tipo_combustivel: Optional[str] = None

    class Config:
        from_attributes = True
