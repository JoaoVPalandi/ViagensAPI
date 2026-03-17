
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CorridaSchema(BaseModel):
    
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: int

    datahora_inicio: Optional[datetime] = None
    datahora_fim: Optional[datetime] = None

    duracao_total: Optional[float] = None

    local_partida: Optional[str] = None
    local_destino: Optional[str] = None

    valor_estimado: Optional[float] = None
    status_corrida: Optional[str] = None