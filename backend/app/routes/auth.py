from fastapi import APIRouter, HTTPException, Response, Form
from app.database import get_db_connection
import bcrypt

router = APIRouter()

@router.post("/login")
def login(
    response: Response,  # ✅ Mueve `response` primero
    email: str = Form(...),  
    password: str = Form(...)  
):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, email, password FROM users WHERE email = %s;", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            response.set_cookie(key="user_id", value=user["id"], httponly=True)  # 🔒 Cookie segura
            return {"message": "Login exitoso"}
        else:
            raise HTTPException(status_code=400, detail="Email o contraseña incorrectos")
    else:
        raise HTTPException(status_code=500, detail="Error de conexión con la base de datos")
