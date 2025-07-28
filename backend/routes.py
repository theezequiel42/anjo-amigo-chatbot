from fastapi import APIRouter
from models import Message
from knowledge.base import knowledge_base
from utils.text import normalize
from services.gemini import generate_response_with_gemini

router = APIRouter()

@router.post("/api/send")
async def send_message(msg: Message):
    user_input = normalize(msg.text)

    # Busca local
    for key in knowledge_base:
        if normalize(key) in user_input:
            return {"messages": knowledge_base[key]}

    # Gemini fallback
    try:
        messages = generate_response_with_gemini(msg.text)
        return {"messages": messages}
    except Exception as e:
        return {"error": f"Erro ao processar com Gemini: {str(e)}"}
