from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import Optional, List

class TodoCoffee(BaseModel):
    name: str
    validity: str
    description: str

app = FastAPI(title='Todo coffee API')

# CRUD (Create, Read, Update, Delete)

store_coffee = []

@app.get('/')
async def get_coffee():
    return {'Quero': 'cafééééé!!!'}

@app.post('/post-coffee/')
async def post_coffee(todo_coffee: TodoCoffee):
    store_coffee.append(todo_coffee)
    return todo_coffee

@app.get('/get-all-coffees/', response_model=List[TodoCoffee])
async def get_all_coffee():
    return store_coffee

@app.get('/get-coffee/{id}')
async def get_coffee(id: int):
    try:
        return store_coffee[id]
    except:
        raise HTTPException(status_code=404, detail='Coffee not found')
    
@app.put('/update-coffee/{id}')
async def update_coffee(id: int, coffee: TodoCoffee):
    try:
        store_coffee[id] = coffee
        return store_coffee[id]
    except:
        raise HTTPException(status_code=404, detail='Coffee not found')
    
@app.delete('/delete-coffee/{id}')
async def delete_coffee(id: int, coffee: TodoCoffee):
    try:
        coffee = store_coffee[id]
        store_coffee.pop(id)
        return coffee
    except:
        raise HTTPException(status_code=404, detail='Coffee not found')
        