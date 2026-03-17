from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.modelo_veiculo import ModeloVeiculoModel
from app.schema.modelo_veiculo import ModeloVeiculoSchema

modelo_veiculo = APIRouter()

@modelo_veiculo.post("/")
async def criar_modelo_veiculo(dados: ModeloVeiculoSchema, db:
                                Session = Depends(get_db)):
    novo_modelo = ModeloVeiculoModel(**dados.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    return novo_modelo

@modelo_veiculo.get("/modelos")
async def listar_modelos(db: Session = Depends(get_db)):
    modelos = db.query(ModeloVeiculoModel).all()
    return modelos

@modelo_veiculo.delete("/delete/{id}")
async def deletar_modelo(id: int, db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel
                                                .id_modelo_veiculo 
                                                == id).first()

    if not modelo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"MModelo de veículo com ID {id} não encontrado"
            )
    
    db.delete(modelo)
    db.commit()
    return('Pronto, id deletado')

@modelo_veiculo.put("/update/{id}")
async def atualizar_modelo(id: int, dados: ModeloVeiculoSchema,
                            db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.
                                         id_modelo_veiculo == id).first()

    if not modelo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"MModelo de veículo com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(modelo, campo, valor)
    
    db.commit()
    db.refresh(modelo)

    return modelo


