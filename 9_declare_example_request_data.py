# Declare Request Example Data

from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Annotated
app = FastAPI()


# class Item(BaseModel):
#     # Field additional arguments example in Field
#     name: str = Field(examples=["Foo"])
#     description: Union[str, None] = Field(default=None, examples=["A very nice Item"])
#     price: float = Field(examples=[35.4])
#     tax: Union[float, None] = Field(default=None, examples=[3.2])

    #example with scema json
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # } 


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Body with examples

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             examples=[
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#                 {
#                     "name": "Bar",
#                     "price": "35.4",
#                 },
#                 {
#                     "name": "Baz",
#                     "price": "thirty five point four",
#                 },
#             ],
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# Using the openapi_examples Parameter
    
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results