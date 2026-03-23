from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.tipo_combustivel import TipoCombustivelModel
from app.schema.tipo_combustivel import TipoCombustivelSchema

tipo_combustivel = APIRouter()

@tipo_combustivel.post("/")
async def criar_pagamento(dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    novo_combustivel = TipoCombustivelModel(**dados.model_dump())
    db.add(novo_combustivel)
    db.commit()
    db.refresh(novo_combustivel)
    return novo_combustivel

@tipo_combustivel.get("/combustivel")
async def listar_combustiveis(db: Session = Depends(get_db)):
    combustiveis = db.query(TipoCombustivelModel).all()
    return combustiveis


@tipo_combustivel.delete("/delete/{id}")
async def deletar_cmbustivel(id: int, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id).first()

    if not tipo_combustivel:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Combustivel com ID {id} não encontrado"
            )
    
    db.delete(tipo_combustivel)
    db.commit()
    return('Pronto, id deletado')

@tipo_combustivel.put("/update/{id}")
async def atualizar_servico(id: int, dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_servico == id).first()

    if not tipo_combustivel:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Serviço com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(tipo_combustivel, campo, valor)
    
    db.commit()
    db.refresh(tipo_combustivel)

    return tipo_combustivel