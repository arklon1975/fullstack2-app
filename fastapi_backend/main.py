from fastapi_backend import config
from fastapi_backend.routers import todos
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Depends
from functools import lru_cache
from typing import Union
from fastapi_backend.routers import todos



import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# routers: comment out next line till create them


app = FastAPI()

# router: comment out next line till create it
app.include_router(todos.router)


origins = [
    "http://localhost:3000",
    "https://todo-frontend-khaki.vercel.app/",
]

# CORS configuration, needed for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#  global http exception handler, to handle errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# # to use the settings


@lru_cache()
def get_settings():
    return config.Settings()

# ENDPOINTS


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # print the app_name configuration
    print(settings.app_name)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
