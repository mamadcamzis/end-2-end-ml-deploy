import typing as t

from fastapi  import FastAPI 
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home_page():
    return {"Message": "Hello World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id", user_id}



class ModelName(str, Enum):
    ALEXNET = "ALEXNET"
    RESNET = "RESNET"
    LENET = "LENET"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name}
    elif model_name.value == "LENET":
        return {"model_name": "Good Choice: lenet"}
    else:
        return {"model_name": f"You have selected {model_name.value}"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

dummy_db = [{"item_name": "t-shirt"}, {"item_name": "shoe"}, {"item_name": "watch"}]

@app.get("/items/")
async def read_items(skip: int=0, limit: int=10, optional_parameter: t.Optional[int]=None):
    return {"items": dummy_db[skip:skip+limit],
            "optional_parameter": optional_parameter}


class Book(BaseModel):
    name: str
    author: str
    description: t.Optional[str] = None
    price: float


@app.post("/books/")
async def create_item(book: Book):
    return book
