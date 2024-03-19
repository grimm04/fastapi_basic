from typing import Any, List, Union

from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse
app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str
# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> List[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]

# response_model

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item


# @app.get("/items/", response_model=List[Item])
# async def read_items() -> Any:
#     return [
#         {"name": "Portal Gun", "price": 42.0},
#         {"name": "Plumbus", "price": 32.0},
#     ]

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

# Return a Response Directly

# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# Annotate a Response Subclass
@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Invalid Return Type Annotations

# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Union[Response, dict]:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}

# Disable Response Model
@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

# Response Model encoding parameters

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]