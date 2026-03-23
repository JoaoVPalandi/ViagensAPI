from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.usuario import UsuarioModel
from app.schema.usuario import UsuarioSchema

usuario = APIRouter()

@usuario.post("/")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@usuario.get("/usuario")
async def listar_servico(db: Session = Depends(get_db)):
    servicos = db.query(UsuarioModel).all()
    return servicos


@usuario.delete("/delete/{id}")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()

    if not usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Usuario com ID {id} não encontrado"
            )
    
    db.delete(usuario)
    db.commit()
    return('Pronto, id deletado')

@usuario.put("/update/{id}")
async def atualizar_servico(id: int, dados: UsuarioSchema, db: Session = Depends(get_db)):
    Usuario = db.query(UsuarioModel).filter(UsuarioModel.id_servico == id).first()

    if not Usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Usuario com ID {id} não encontrado"
            )

    for campo, valor in dados.model_dump().items():
        setattr(Usuario, campo, valor)
    
    db.commit()
    db.refresh(Usuario)

    return Usuario