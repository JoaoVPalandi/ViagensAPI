from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.metodo_pagamento import MetodoPagamentoModel
from app.schema.metodo_pagamento import MetodoPagamentoSchema

metodo_pagamento = APIRouter()

@metodo_pagamento.post("/")
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo = MetodoPagamentoModel(**dados.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)
    return novo_metodo

@metodo_pagamento.get("/metodos")
async def listar_metodos(db: Session = Depends(get_db)):
    metodos = db.query(MetodoPagamentoModel).all()
    return metodos

@metodo_pagamento.delete("/delete/{id}")
async def deletar_metodo(id: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id).first()

    if not metodo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Método de pagamento com ID {id} não encontrado"
            )
    
    db.delete(metodo)
    db.commit()
    return('Pronto, id deletado')

@metodo_pagamento.put("/update/{id}")
async def atualizar_metodo(id: int, dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id).first()

    if not metodo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Método de pagamento com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(metodo, campo, valor)
    
    db.commit()
    db.refresh(metodo)

    return metodo


