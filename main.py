from controller import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API REST",
    description="API para consulta e manipulação das comunicações de perda do Proagro fácil.",
    version="0.0.1",
    contact={
        "name": "Simeone Johnson"
    }
)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
