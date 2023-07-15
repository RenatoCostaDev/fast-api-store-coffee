from fastapi import FastAPI, Form
from pydantic import BaseModel 


app = FastAPI()

@app.post('/coffee/')
async def form_cafeeee(name: str = Form(...), year: str = Form(...)):
    return { 
            'name': name,
            'year': year,
    } 