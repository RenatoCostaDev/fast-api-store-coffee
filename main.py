from fastapi import FastAPI, HTTPException
from models import Candie, CandieIn_Pydantic, Candie_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

class Message(BaseModel):
    message: str


app = FastAPI()

@app.get('/')
async def quero_cafeeee():
    return { 'quero': 'cafééééé!!!!'}

@app.post('/candie', response_model=Candie_Pydantic)
async def create(candie: CandieIn_Pydantic):
    obj = await Candie.create(**candie.dict(exclude_unset=True))
    return await Candie_Pydantic.from_tortoise_orm(obj)

# KeyError: '__module__'
# to be resolve ...

register_tortoise(
    app,
    db_url="sqlite://candie.db",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)