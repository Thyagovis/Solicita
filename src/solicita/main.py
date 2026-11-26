from fastapi import FastAPI
from contextlib import asynccontextmanager
from agents.controller import router

@asynccontextmanager
async def lifespan(app : FastAPI):

    print("iniciando aplicação...")

    yield

    print("encerrando aplicação...")

app = FastAPI(lifespan = lifespan)

app.include_router(router)