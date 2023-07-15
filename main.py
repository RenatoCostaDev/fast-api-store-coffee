from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel # Não precisa pip install, todos os atributos e data serão herdados daqui

class Coffee(BaseModel):
    nome:str
    tipo: str
    descricao: Optional[str] = None

app = FastAPI()

@app.get('/')                           
async def quero_cafeeee():
    return { 'quero': 'cafééééé!!!!'}

# @app.post('/coffee/')
# async def make_coffee(coffee: Coffee):
#     return coffee

@app.post('/coffee/{nivel}')
async def make_coffee(coffee: Coffee, nivel: int, value: bool):
    return {**coffee.model_dump(), 'nivel': nivel, 'value': value}

'''
    return {'coffee': coffee, 'nivel': nivel, 'value': value}

{
  "coffee": {
    "nome": "3 corações",
    "tipo": "forte",
    "descricao": "acorda urso hibernando!!Cuidado!!"
  },
  "nivel": 1,
  "value": true
}
'''