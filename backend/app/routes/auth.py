from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
def login():
    return {"message": "Ruta de login"}

@router.get("/register")
def register():
    return {"message": "Ruta de registro"}
