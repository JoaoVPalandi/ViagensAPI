from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serviço import ServicoModel
from app.schema.serviço import ServicoSchema

servico = APIRouter()

@servico.post("/")
async def criar_servicos(dados: ServicoSchema, db: Session = Depends(get_db)):
    novo_servico = ServicoModel(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/servicos")
async def listar_servico(db: Session = Depends(get_db)):
    servicos = db.query(ServicoModel).all()
    return servicos


@servico.delete("/delete/{id}")
async def deletar_servico(id: int, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id).first()

    if not servico:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Servico com ID {id} não encontrado"
            )
    
    db.delete(servico)
    db.commit()
    return('Pronto, id deletado')

@servico.put("/update/{id}")
async def atualizar_servico(id: int, dados: ServicoSchema, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id).first()

    if not servico:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Serviço com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(servico, campo, valor)
    
    db.commit()
    db.refresh(servico)

    return servico