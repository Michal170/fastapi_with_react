from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ustawienie "*" pozwala na żądania z dowolnego źródła
    allow_credentials=True,
    allow_methods=["*"],  # Pozwolenie na wszystkie metody HTTP
    allow_headers=["*"],  # Pozwolenie na wszystkie nagłówki
)


@app.get("/")
async def root():
    return { "message":"Hello World"}

@app.get("/home")
async def root(name: str = "Test", surname: str = "Name"):
    return { f"Welcome on home page {name} {surname}"}

@app.get("/todo")
async def get_todos()-> dict:
    return{"data":todos}

todos = [
    {
        "id":"1",
        "item": "Read a book"
    },
        {
        "id":"2",
        "item": "Ride a bike"
    },
]