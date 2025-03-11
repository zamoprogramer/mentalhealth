from fastapi import APIRouter
from app.utils.db_queries import insert_user, get_users, insert_message

router = APIRouter()

# Route to create a new user
@router.post("/insert_user")
def create_user(email: str, password: str, first_name: str, last_name: str):
    print(email, password, first_name, last_name)
    return insert_user(email, password, first_name, last_name)

# Route to get all users
@router.get("/get_users")
def list_users():
    return get_users()

# Route to insert a message
@router.post("/insert_message")
def create_user(email: str, password: str, first_name: str, last_name: str):
    return insert_user(email, password, first_name, last_name)

