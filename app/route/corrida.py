from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.corrida import CorridaModel
from app.schema.corrida import CorridaSchema

corrida = APIRouter()

@corrida.post("/")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/corridas")
async def listar_corridas(db: Session = Depends(get_db)):
    corridas = db.query(CorridaModel).all()
    return corridas

@corrida.delete("/delete/{id}")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Corrida com ID {id} não encontrada"
            )
    
    db.delete(corrida)
    db.commit()
    return('Pronto, id deletado')

@corrida.put("/update/{id}")
async def atualizar_corrida(id: int, dados: CorridaSchema, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Corrida com ID {id} não encontrada"
            )

    for campo, valor in dados.model_dump().items():
        setattr(corrida, campo, valor)
    
    db.commit()
    db.refresh(corrida)

    return corrida


