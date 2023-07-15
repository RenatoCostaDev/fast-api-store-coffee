from fastapi import FastAPI
from typing import Optional


app = FastAPI()                      # uvicorn main:app --reload

@app.get('/')                           
async def quero_cafeeee():
    return { 'quero': 'cafééééé!!!!'}


@app.get('/cafe/{cafe_id}')          # path parameter
async def get_cofee(cafe_id: int):   # : int -> sem isso pode passar qq item, str qq
    return { 'cafe_id' : cafe_id}


@app.get('/cafe/')                               # 'http://127.0.0.1:8000/cafe/?number=1&text=capuccino' \
async def read_cafe(number: int, text: Optional[str]):     # query parameter   # http://127.0.0.1:8000/cafe/?number=1&text=
    return {
        'number': number,
        'text': text
    }