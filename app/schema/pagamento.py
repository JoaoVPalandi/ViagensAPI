from pydantic import BaseModel
from typing import Optional

class PagamentoSchema(BaseModel):
    valor: Optional[float] = None
    data_pagamento: Optional[str] = None
    id_metodo_pagamento: int
    id_corrida: int 

    class Config:
        from_attributes = True