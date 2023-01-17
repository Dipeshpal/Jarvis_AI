from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def start_gui():
    uvicorn.run("app:JarvisAI/services/gui/app", host="127.0.0.1", port=8000, reload=True)

