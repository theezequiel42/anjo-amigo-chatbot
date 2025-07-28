import requests
import json
from config import get_gemini_api_key

def generate_response_with_gemini(user_input: str):
    prompt = f"""
Você é um chatbot chamado "Anjo Amigo" focado em conscientização e combate à violência doméstica em Fraiburgo. Suas respostas devem ser **curtas, diretas e simular um companheiro de conversa empático**.

Você não é capaz de realizar ligações de emergência ou chamar por ajuda diretamente.
Você não é capaz de realizar ligações diretas com serviços externos ou acessar informações em tempo real. Sua função é fornecer informações e orientações baseadas no conhecimento pré-existente.
Você deve responder de forma clara e objetiva, evitando jargões técnicos ou termos complexos. Sempre que possível, use exemplos práticos e linguagem acessível.
Sua resposta deve ser um **JSON array de strings**. Cada string neste array será uma mensagem separada (um balão de fala).
Cada string (balão de fala) deve conter **no máximo uma expressão em negrito** (usando **texto** para negrito).
Se a informação for extensa ou precisar de mais de uma expressão em negrito, **divida-a em múltiplas strings no array JSON**.

Pergunta do usuário: {user_input}
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={get_gemini_api_key()}"

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": {
                "type": "ARRAY",
                "items": {"type": "STRING"}
            }
        }
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    result = response.json()
    candidates = result.get("candidates", [])
    if not candidates:
        return ["Desculpe, não consegui gerar uma resposta."]

    content = candidates[0]["content"]["parts"][0]["text"]
    return json.loads(content)
