import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database credentials
DB_HOST = os.getenv("MYSQL_HOST")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_PORT = int(os.getenv("MYSQL_PORT", 3306))

def test_connection():
    try:
        print("Intentando conectar a la base de datos...")
        print(f"Host: {DB_HOST}")
        print(f"Puerto: {DB_PORT}")
        print(f"Base de datos: {DB_NAME}")
        print(f"Usuario: {DB_USER}")
        
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            connect_timeout=30,  # Aumentamos el timeout a 30 segundos
            use_pure=True  # Usar implementación pura de Python
        )
        
        if conn.is_connected():
            print("✅ Conexión exitosa a la base de datos!")
            db_info = conn.get_server_info()
            print(f"Versión del servidor MySQL: {db_info}")
            
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE();")
            database = cursor.fetchone()
            print(f"Base de datos conectada: {database[0]}")
            
            cursor.close()
            conn.close()
            print("Conexión cerrada.")
            
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")

if __name__ == "__main__":
    test_connection()
