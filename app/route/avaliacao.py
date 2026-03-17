from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.avaliacao import AvaliacaoModel
from app.schema.avaliacao import AvaliacaoSchema

avaliacao = APIRouter()

@avaliacao.post("/")
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    nova_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

@avaliacao.get('/avaliações')
async def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()

@avaliacao.delete('/delete/{id}')
async def deletar_avaliacao(id: int, db: Session = Depends(get_db)):
   id = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id).first()

   if not id:
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Avaliação com ID {id} não encontrada"
            )
   
   db.delete(id)
   db.commit()
   return('Pronto, id deletado')

@avaliacao.get('/update/{id}')
async def atualizar_avaliacao(id: int, dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    avaliacao = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id).first()

    if not avaliacao:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Avaliação com ID {id} não encontrada"
            )

    for campo, valor in dados.model_dump().items():
        setattr(avaliacao, campo, valor)
    
    db.commit()
    db.refresh(avaliacao)

    return avaliacao