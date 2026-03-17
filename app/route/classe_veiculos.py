from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.classe_veiculo import ClasseModel
from app.schema.classe_veiculo import ClasseSchema

classe_veiculo = APIRouter()

@classe_veiculo.post("/")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    nova_classe = ClasseModel(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe_veiculo.get("/classes")
async def listar_classes(db: Session = Depends(get_db)):
    classes = db.query(ClasseModel).all()
    return classes

@classe_veiculo.delete("/delete/{id}")
async def deletar_classe(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Classe de veículo com ID {id} não encontrada"
            )
    
    db.delete(classe)
    db.commit()
    return('Pronto, id deletado')

@classe_veiculo.put("/update/{id}")
async def atualizar_classe(id: int, dados: ClasseSchema, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Classe de veículo com ID {id} não encontrada"
            )

    for campo, valor in dados.model_dump().items():
        setattr(classe, campo, valor)
    
    db.commit()
    db.refresh(classe)

    return classe


