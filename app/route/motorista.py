from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista import Motorista
from app.schema.motorista import MotoristaSchema

motorista = APIRouter()

##----------------------------------------------------------------------------##

# Criar um novo motorista

@motorista.post("/")
async def criar_motorista(motorista: MotoristaSchema, db: Session = Depends(get_db)):
    novo_motorista = Motorista(**motorista.model_dump())
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista

##----------------------------------------------------------------------------##

# Listar todos os motoristas

@motorista.get("/listar")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(Motorista).all()

##----------------------------------------------------------------------------##

# Deletar um motorista por ID

@motorista.delete("/deletar/{id}")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    motorista = db.query(Motorista).filter(Motorista.id_motorista == id).first()

    if not motorista:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O motorista com ID {id} não foi encontrado")
    
    db.delete(motorista)
    db.commit()
    return("deletado")

##----------------------------------------------------------------------------##

# Atualizar um motorista por ID

@motorista.put("/atualizar/{id}")
async def atualizar_motorista(id: int, motorista: MotoristaSchema, db: Session = Depends(get_db)):
    motorista_atualizar = db.query(Motorista).filter(Motorista.id_motorista == id).first()

    if not motorista_atualizar:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O motorista com ID {id} não foi encontrado")
    
    for key, value in motorista.model_dump().items():
        setattr(motorista_atualizar, key, value)
    db.commit()
    db.refresh(motorista_atualizar)
    return motorista_atualizar



