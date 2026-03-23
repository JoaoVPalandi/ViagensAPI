from sqlalchemy import Column, BigInteger, String, Date, Integer
from app.database import Base


class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(255))
    cpf = Column(String(11))
    idade = Column(Integer)
    data_nascimento = Column(Date)
    senha = Column(String(64))
    email = Column(String(255))
    username = Column(String(50))