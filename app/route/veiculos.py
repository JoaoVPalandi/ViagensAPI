from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.veiculos import VeiculoModel
from app.schema.veiculos import VeiculoSchema

veiculo = APIRouter()

##----------------------------------------------------------------------------##

## Criar um novo veículo

@veiculo.post("/")
async def criar_veiculo(veiculo: VeiculoSchema, db: Session = Depends(get_db)):
    novo_veiculo = VeiculoModel(**veiculo.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo

##----------------------------------------------------------------------------##

# Listar todos os veículos

@veiculo.get("/listar")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()

##----------------------------------------------------------------------------##

# Deletar um veículo por ID

@veiculo.delete("/deletar/{id}")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()

    if not veiculo:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O veículo com ID {id} não foi encontrado")
    
    db.delete(veiculo)
    db.commit()
    return("deletado")

##----------------------------------------------------------------------------##

# Atualizar um veículo por ID

@veiculo.put("/atualizar/{id}")
async def atualizar_veiculo(id: int, veiculo: VeiculoSchema, db: Session = Depends(get_db)):
    veiculo_atualizar = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()

    if not veiculo_atualizar:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"O veículo com ID {id} não foi encontrado")
    
    for key, value in veiculo.model_dump().items():
        setattr(veiculo_atualizar, key, value)
        db.commit()
        db.refresh(veiculo_atualizar)
        return veiculo_atualizar