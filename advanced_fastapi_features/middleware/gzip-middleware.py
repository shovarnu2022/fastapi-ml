from fastapi import FastAPI
from starlette.middleware.cors import GZipMiddleware

app = FastAPI()

app.add_middleware(
    GZipMiddleware, minimum_size=1000
)



