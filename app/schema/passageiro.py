from pydantic import BaseModel
from typing import Optional

class PassageiroSchema(BaseModel):
    id_usuario: int
    media_avaliacao: Optional[float] = None

    class Config:
        from_attributes = True