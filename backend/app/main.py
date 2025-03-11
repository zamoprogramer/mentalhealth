from fastapi import FastAPI
from app.routes import auth, db_test
from app.database import initialize_database  # Corregir la importación

app = FastAPI()

# Inicializa la base de datos (descomenta si necesitas ejecutar esto)
initialize_database()

# Incluir rutas de autenticación y base de datos
app.include_router(auth.router)
app.include_router(db_test.router, prefix="/db_test", tags=["Database"])

@app.get("/")
def home():
    return {"message": "Backend funcionando correctamente"}
