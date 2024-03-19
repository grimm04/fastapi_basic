from typing import List, Union

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Union[str, None] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#add validation with Annotated for q(params) q: Annotated[Union[str, None]] = None , Query 
# @app.get("/items/")
# async def read_items(
#     #optional
#     # q: Annotated[Union[str, None], Query(min_length=3, max_length=50)] = None
#     #required Ellipsis ...
#     # q: Annotated[str, Query(min_length=3)]
#     # q: Annotated[str, Query(min_length=3)] = ...
#     #Required with None
#     q: Annotated[Union[str, None], Query(min_length=3)] = ...
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# Add regular expressions

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         Union[str, None], Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#Query parameter list / multiple values
# @app.get("/items/") 
# # async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
# async def read_items(q: Annotated[list, Query()] = []):
#     query_items = {"q": q}
#     return query_items

# Declare more metadata
# add title to Query
# @app.get("/items/")
# async def read_items(
#     q: Annotated[Union[str, None], Query(title="Query string", min_length=3)] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# add description
# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         Union[str, None],
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Alias parameters

# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(alias="item-query")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Deprecating parameters

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         Union[str, None],
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True,
#         ),
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Exclude from OpenAPI 

# @app.get("/items/")
# async def read_items(
#     hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     else:
#         return {"hidden_query": "Not found"}