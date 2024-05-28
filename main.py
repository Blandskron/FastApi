from fastapi import FastAPI

app = FastAPI()
app.title = "Api"
app.version = "0.01"

@app.get('/', tags=['Home'])
def message():
    return "Hello world!"

