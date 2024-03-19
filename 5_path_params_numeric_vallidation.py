from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()

# Declare metadata
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[Union[str, None], Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

#kwargs necesery use Annotated

# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
 
# Number validations: greater than or equal
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Number validations: floats, greater than and less than

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results