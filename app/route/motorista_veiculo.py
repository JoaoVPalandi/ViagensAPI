from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista_veiculo import MotoristaVeiculoModel
from app.schema.motorista_veiculo import MotoristaVeiculoSchema

motorista_veiculo = APIRouter()

@motorista_veiculo.post("/{id_motorista}/{id_veiculo}")
async def associar_motorista_veiculo(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    novo_motorista_veiculo = MotoristaVeiculoModel(id_motorista=id_motorista, id_veiculo=id_veiculo)
    db.add(novo_motorista_veiculo)
    db.commit()
    db.refresh(novo_motorista_veiculo)

    return {"message": f"{novo_motorista_veiculo} associação ao veículo com sucesso."}


@motorista_veiculo.get("/listar")
async def listar_motorista_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()


@motorista_veiculo.delete("/deletar/{id_motorista}/{id_veiculo}")
async def deletar_motorista_veiculo(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista == id_motorista, MotoristaVeiculoModel.id_veiculo == id_veiculo).first()

    if not motorista_veiculo:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O motorista_veiculo com ID {id_motorista} e ID {id_veiculo} não foi encontrado")
    
    db.delete(motorista_veiculo)
    db.commit()
    return("deletado")

@motorista_veiculo.put("/atualizar/{id_motorista}/{id_veiculo}")
async def atualizar_motorista_veiculo(id_motorista: int, id_veiculo: int, motorista_veiculo: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    motorista_veiculo_atualizar = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista == id_motorista, MotoristaVeiculoModel.id_veiculo == id_veiculo).first()

    if not motorista_veiculo_atualizar:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O motorista_veiculo com ID {id_motorista} e ID {id_veiculo} não foi encontrado")
    
    for key, value in motorista_veiculo.model_dump().items():
        setattr(motorista_veiculo_atualizar, key, value)
