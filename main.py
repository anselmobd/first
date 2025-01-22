from fastapi import FastAPI
from model import User
from database import Users


app = FastAPI()
users = Users()


@app.get('/')
def index():
    return {"message": "Hello World"}


@app.post('/users')
def createUser(user: User):
    users.add_user(user)
    users.pprint() 
    return {'user': user}
