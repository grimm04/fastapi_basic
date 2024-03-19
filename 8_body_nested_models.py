# Body – Nested models
from typing import Union, List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    #this one 
    # tags: list = []
    # Lists with type parameters as fields before 3.9
    # tags: List[str] = []
    # Set types
    tags: Set[str] = set()
    # nested image model
    # Attributes with lists of child models
    images: Union[List[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results




# Deeply nested models
@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# Bodysuits from pure lists
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

# Bodysuits with any dicts

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights