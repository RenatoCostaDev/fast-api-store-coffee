from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel # Não precisa pip install, todos os atributos e data serão herdados daqui

class CoffeeIn(BaseModel):
    secret_id: int            # Não aparece na url -> http://127.0.0.1:8000/coffee/
    nome:str
    tipo: str
    descricao: Optional[str] = None

class Coffee(BaseModel):
    nome:str
    tipo: str
    descricao: Optional[str] = None

app = FastAPI()

@app.get('/')                           
async def quero_cafeeee():
    return { 'quero': 'cafééééé!!!!'}


# @app.post('/coffee/', response_model=Coffee)
# async def make_coffee(coffee: CoffeeIn):
#     return coffee

# @app.post('/coffee/', response_model=Coffee, response_model_include={'tipo'})
# async def make_coffee(coffee: CoffeeIn):
#     return coffee

'''
{
  "tipo": "fromHell"
}
'''
@app.post('/coffee/', response_model=Coffee, response_model_exclude={'tipo'})
async def make_coffee(coffee: CoffeeIn):
    return coffee

'''
{
  "nome": "3 corações",
  "descricao": "burns like hell!!"
}
'''