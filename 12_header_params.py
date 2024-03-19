# Header Parameters

from typing import Union, List

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()

#disalbe convert too - Header(convert_underscores=False)
# @app.get("/items/")
# async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
#     return {"User-Agent": user_agent}

# Duplicate headers
@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}