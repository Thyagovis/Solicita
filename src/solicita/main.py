from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):

    print("iniciando aplicação...")

    yield

    print("encerrando aplicação...")

app = FastAPI(lifespan = lifespan)