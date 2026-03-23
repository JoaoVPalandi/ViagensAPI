from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.passageiro import PassageiroModel
from app.schema.passageiro import PassageiroSchema

passageiro = APIRouter()

@passageiro.post("/")
async def criar_passageiros(dados: PassageiroSchema, db: Session = Depends(get_db)):
    novo_passageiro = PassageiroModel(**dados.model_dump())
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@passageiro.get("/passageiro")
async def listar_passageiros(db: Session = Depends(get_db)):
    passageiros = db.query(PassageiroModel).all()
    return passageiros  


@passageiro.delete("/delete/{id}")
async def deletar_passageiros(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Passageiro com ID {id} não encontrado"
            )
    
    db.delete(passageiro)
    db.commit()
    return('Pronto, id deletado')

@passageiro.put("/update/{id}")
async def atualizar_passageiro(id: int, dados: PassageiroSchema, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Passageiro com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(passageiro, campo, valor)
    
    db.commit()
    db.refresh(passageiro)

    return passageiro