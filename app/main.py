from fastapi import FastAPI
from app.database import engine, Base

##---------------------------MODULOS DAS ROTAS--------------------------------##

from app.route.classe_veiculos import classe_veiculo
from app.route.avaliacao import avaliacao
from app.route.pagamento import pagamento
from app.route.metodo_pagamento import metodo_pagamento
from app.route.corrida import corrida
from app.route.modelo_veiculo import modelo_veiculo
from app.route.motorista_veiculo import motorista_veiculo
from app.route.motorista import motorista
from app.route.passageiro import passageiro
from app.route.serviço import servico
from app.route.tipo_combustivel import tipo_combustivel
from app.route.usuario import usuario
from app.route.veiculos import veiculo

##----------------------------------------------------------------------------##
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(avaliacao, prefix="/avaliacao", tags=["Avaliação"])
app.include_router(classe_veiculo, prefix="/classe_veiculo", tags=["Classe Veículo"])
app.include_router(pagamento, prefix="/pagamento", tags=["Pagamento"])
app.include_router(metodo_pagamento, prefix="/metodo_pagamento", tags=["Método de Pagamento"])
app.include_router(corrida, prefix="/corrida", tags=["Corrida"])
app.include_router(modelo_veiculo, prefix="/modelo_veiculo", tags=["Modelo de Veículo"])
app.include_router(motorista_veiculo, prefix="/motorista_veiculo", tags=["Motorista Veículo"])
app.include_router(motorista, prefix="/motorista", tags=["Motorista"])
app.include_router(passageiro, prefix="/passageiro", tags=["Passageiro"])
app.include_router(servico, prefix="/servico", tags=["Serviço"])
app.include_router(tipo_combustivel, prefix="/tipo_combustivel", tags=["Tipo Combustível"])
app.include_router(usuario, prefix="/usuario", tags=["Usuário"])
app.include_router(veiculo, prefix="/veiculo", tags=["Veículo"])


@app.get("/")
def read_root():
    return {"hello": "palandi"}



