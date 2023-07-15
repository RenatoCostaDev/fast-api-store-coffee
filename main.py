from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def quero_cafeeee():
    return { 'quero': 'cafééééé!!!!'}