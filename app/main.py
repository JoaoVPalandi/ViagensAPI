from fastapi import FastAPI
from app.route.avaliacao import avaliacao
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(avaliacao, prefix="/avaliacao", tags=["Avaliação"])

@app.get("/")
async def root():
    return {"message": "Hello World"}




