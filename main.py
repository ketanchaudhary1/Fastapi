from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app=FastAPI()
@app.get('/')
def home():
    return {"message": "My name is KETAN"}
@app.get('/about')
def about():
    return {"message": "I am a software developer."}
@app.get('/users')
def users():
    return {"message": "I have 5 years of experience in software development."}

@app.post("/create-user")
def create_user(users: User):

    return {"message": f"User {users.name} created successfully with age {users.age}"}