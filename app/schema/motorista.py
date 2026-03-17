from pydantic import BaseModel
from typing import Optional


class MotoristaSchema (BaseModel):
    __tablename__ = "motorista"

    media_avaliacao: Optional [float] = None
    cnh: int 