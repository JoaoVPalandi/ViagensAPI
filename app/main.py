from fastapi import FastAPI
# from app.route.avaliacao import avaliacao

app = FastAPI()
# app.include_router(avaliacao)

@app.get("/")
async def root():
    return {"message": "Hello World"}




