from sqlalchemy import Column, Integer, String
from app.database import Base


class MetodoPagamentoModel(Base):
    __tablename__ = "metodo_pagamento"

    id_metodo_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(45))
    nome_financeira = Column(String(45))