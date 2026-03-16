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



