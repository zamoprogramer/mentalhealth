from app.database import get_db_connection  # Importa la conexión a la base de datos

import bcrypt

def insert_user(email: str, password: str, first_name: str, last_name: str):
    conn = get_db_connection()
    if conn:
        if email_exists(email):  # ❌ Si el correo ya existe, devolvemos un error
            return {"error": "Email already exists"}

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  # 🔒 Cifrar contraseña

        cursor = conn.cursor()
        sql = "INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, (email, hashed_password.decode('utf-8'), first_name, last_name))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "User inserted successfully"}
    else:
        return {"error": "Database connection failed"}
def get_users():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, first_name, last_name, email, password, created_at FROM users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    else:
        return {"error": "Database connection failed"}

def insert_message(user_id: int, message: str):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO messages (user_id, message) VALUES (%s, %s);"
        cursor.execute(sql, (user_id, message))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Message inserted successfully"}
    else:
        return {"error": "Database connection failed"}

def email_exists(email: str):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM users WHERE email = %s;"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()[0]  # Obtiene el número de registros con ese email
        cursor.close()
        conn.close()
        return result > 0  # Devuelve True si el correo ya existe, False si no
    else:
        return False  # Si hay error en la base de datos, asumimos que no existe

