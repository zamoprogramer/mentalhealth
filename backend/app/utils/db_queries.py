from app.database import get_db_connection

def insert_user(email: str, password: str, first_name: str, last_name: str):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, (email, password, first_name, last_name))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "User inserted successfully"}
    else:
        return {"error": "Database connection failed"}

# Function to get all users
def get_users():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, username, created_at FROM users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"users": users}
    else:
        return {"error": "Database connection failed"}

# Function to insert a message
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
