from fastapi import FastAPI
from app.routes import auth, chat, history

app = FastAPI()

# Incluir rutas (endpoints)
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(history.router)

@app.get("/")
def home():
    return {"message": "Backend funcionando correctamente"}

# Para correr el servidor: uvicorn app.main:app --reload
