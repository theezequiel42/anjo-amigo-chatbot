from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import load_settings
from routes import router

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de status (raiz)
@app.get("/")
async def root():
    return {"message": "API Anjo Amigo está rodando corretamente!"}

# Configurações e rotas
load_settings()
app.include_router(router)
