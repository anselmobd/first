from fastapi import FastAPI, HTTPException
from model import User, UserData
from database import Users


app = FastAPI()
users = Users()


@app.get('/')
def index():
    return {"message": "Hello World"}


@app.post('/users')
def create_user(user: User):
    users.add_user(user)
    users.pprint() 
    return {'user': user}


@app.put("/users/{id}")
def update_user(id: int, user: UserData):
    if (user := users.update_user(id, user)):
        users.pprint() 
        return user 
    raise HTTPException(status_code=404, detail="User not found.")
