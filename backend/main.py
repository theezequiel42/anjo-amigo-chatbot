from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import load_settings
from routes import router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode ser ajustado
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega configurações e rotas
load_settings()
app.include_router(router)
