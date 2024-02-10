import uvicorn
from fastapi import FastAPI, Response
from models import Item, AddItemRequest, UpdateItemRequest
from data import Data

app = FastAPI()
data = Data()


@app.get("/shopping-list")
async def get():
    return data.get()


@app.get("/shopping-list/{id}")
def getById(id: str):
    i = data.getById(id)
    if i is None:
        return Response(status_code=404)
    return i


@app.post("/shopping-list")
def add(request: AddItemRequest):
    return data.add(request.name, request.quantity)


@app.put("/shopping-list/{id}")
def update(id: str, request: UpdateItemRequest):
    i = data.getById(id)
    if i is None:
        return Response(status_code=404)
    data.update(id, request.name, request.quantity, request.is_done)
    return i


@app.delete("/shopping-list/{id}")
def getById(id: str):
    i = data.getById(id)
    if i is None:
        return Response(status_code=404)
    data.remove(id)
    return Response(status_code=200)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8080,
        log_level="debug",
        reload=True,
    )
