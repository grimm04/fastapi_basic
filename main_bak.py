from typing import Optional

from fastapi import FastAPI

#JSON data model
from pydantic import BaseModel
#instance
app = FastAPI()

#model

#Json Models
class Item(BaseModel):
    name :str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

#method operation
@app.get("/")

#path func
async def root():
    return {"message : Hello World"}

 
#store items
@app.post("/items/")
async def create_item(item : Item): 
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict


#update put
@app.put("/items/{item_id}")
async def create_item(item_id : int, item:Item):
    return {"item_id ":item_id,**item.dict()}

#get by id
@app.get("/item/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}

#user me
@app.get("/user/me")
async def read_user_me():
    return {"user_id : the current user"}

#get user by user_id
@app.get("/read_user/{user_id}")
async def read_user(user_id : int):
    return {"user_id ": user_id}
