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

# Function to connect to MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        return conn
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Function to execute SQL schema file
def initialize_database():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        with open("sql/schemas.sql", "r") as file:
            sql_commands = file.read().split(";")  # Split queries
            for command in sql_commands:
                if command.strip():  # Ignore empty commands
                    cursor.execute(command)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Database schema initialized successfully.")
    else:
        print("❌ Failed to initialize the database.")


