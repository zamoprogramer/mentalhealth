from fastapi import FastAPI
from app.routes import auth, db_test
from app.database import initialize_database

app = FastAPI()

# Initialize database schema
#initialize_database()

# Include routes
app.include_router(auth.router)
from fastapi import FastAPI
from app.routes import db_test

app = FastAPI()

# Ensure this line is present
app.include_router(db_test.router, prefix="/db_test", tags=["Database"])

@app.get("/")
def home():
    return {"message": "Backend funcionando correctamente"}

@app.get("/")
def home():
    return {"message": "Backend funcionando correctamente"}

