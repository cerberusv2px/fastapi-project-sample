from enum import Enum

from fastapi import FastAPI, Path, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


data = [1, 2, 3, 4, 5]


@app.get("/")
async def root():
    return {"message": "hello mfers"}


@app.get("/rx")
async def test():
    return "<h1>Rx</h1>"


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item": data[item_id]}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 0):
    return fake_items_db[skip: skip + limit]


from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = 0.0


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(*,
                      item_id: int = Path(..., title="ID of item to get", ge=0, le=1000),
                      q: Optional[str] = None,
                      item: Optional[Item] = None
                      ):
    print(item_id)
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


from typing import List


class Book(BaseModel):
    id: int
    title: str
    author: str


class Person(BaseModel):
    id: int
    name: str
    books: List[Book]


@app.post("/persons/")
def get_persons(persons: List[Person]):
    print(persons)
    return persons


class AizenException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(AizenException)
async def aizen_exception_handler(request: Request, exc: AizenException):
    return JSONResponse(
        status_code=420,
        content={"message": f"Oops! {exc.name} did something wrong."}
    )


@app.get("/aizen/{name}")
async def read_aizen(name: str):
    if name == 'ichigo':
        raise AizenException(name=name)
    return {"aizen_sama": name}


from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse




@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body()},
                                 )
    )

class Item(BaseModel):
    name: str
    size: int


@app.post("/test-json/")
async def test_json_error(item: Item):
    return item
