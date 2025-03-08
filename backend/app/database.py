import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Obtener credenciales de MySQL
DATABASE_URL = os.getenv("DATABASE_URL")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", 3306)

# Conectar a MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT", 3306)
        )
        print("✅ Conexión exitosa a MySQL")
        return conn
    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
