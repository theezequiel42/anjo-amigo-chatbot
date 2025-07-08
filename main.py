from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
import json
import unicodedata

# Carrega as variáveis de ambiente
load_dotenv()

app = FastAPI()

# Libera CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

# Base de conhecimento local (pode ser expandida depois)
# Base de conhecimento local – Fraiburgo (atualizada)
knowledge_base = {
    "violência física": [
        "A violência física envolve **agressões corporais**.",
        "Em emergências, ligue 190 (Polícia Militar)."
    ],
    "violência psicológica": [
        "A violência psicológica causa **dano emocional**.",
        "O CREAS (49 3246-2826) oferece apoio."
    ],
    "violência sexual": [
        "É qualquer ato sexual **não desejado**.",
        "Para ajuda, contate a Vigilância Epidemiológica (49 3256-4043)."
    ],
    "violência patrimonial": [
        "É a **subtração ou destruição de bens**.",
        "A Secretaria de Assistência Social (49 3908-2025) pode auxiliar."
    ],
    "violência moral": [
        "Inclui **calúnia, difamação ou injúria**.",
        "A OAB por Elas (49 3246-2090) oferece ajuda jurídica."
    ],
    "rede protetiva": [
        "A **Rede Protetiva em Fraiburgo** reúne CREAS, CRAS, CMDM, Secretaria de Assistência Social, Polícias e outros órgãos."
    ],
    "como denunciar": [
        "Para denunciar, ligue **190 (Polícia Militar)**.",
        "Você também pode registrar um B.O. na Polícia Civil - Sala Lilás."
    ],
    "lei maria da penha": [
        "A **Lei Maria da Penha** (Lei nº 11.340/2006) protege vítimas e responsabiliza agressores."
    ],
    "creas": [
        "O **CREAS (49 3246-2826)** oferece atendimento psicossocial e encaminha para benefícios."
    ],
    "cras": [
        "O **CRAS (49 3256-3069)** previne riscos e fortalece vínculos familiares."
    ],
    "secretaria municipal de assistência social": [
        "A **Secretaria Municipal de Assistência Social (49 3908-2025)** gerencia a assistência social e oferece benefícios."
    ],
    "secretaria municipal de educação": [
        "A **Secretaria Municipal de Educação (49 3256-4250)** acolhe crianças/adolescentes vítimas e faz campanhas."
    ],
    "conselho municipal dos direitos da mulher": [
        "O **CMDM (49 3908-2025)** garante controle social e participação popular para direitos das mulheres."
    ],
    "procuradoria especial da mulher": [
        "A **Procuradoria Especial da Mulher (49 3246-2764)** defende a igualdade e recebe denúncias."
    ],
    "secretaria de saúde - unidades de saúde": [
        "As **Unidades de Saúde (49 3256-4000)** acolhem vítimas e comunicam a polícia."
    ],
    "hospital fraiburgo": [
        "O **Hospital Fraiburgo (49 3246-1012)** oferece atendimento humanizado e avaliação psicossocial."
    ],
    "samu": [
        "O **SAMU (192)** presta socorro emergencial.",
        "Ligue em caso de urgência."
    ],
    "vigilância epidemiológica": [
        "A **Vigilância Epidemiológica (49 3256-4043)** atende vítimas de violência sexual e monitora dados."
    ],
    "polícia civil - sala lilás": [
        "A **Polícia Civil - Sala Lilás (49 3533-5456)** investiga crimes, registra B.O. e medidas protetivas."
    ],
    "polícia militar - rede catarina": [
        "A **Polícia Militar (190)** tem a Rede Catarina para prevenção.",
        "Oferece visitas e o 'botão do pânico'."
    ],
    "corpo de bombeiros": [
        "O **Corpo de Bombeiros (193)** presta socorro de emergência.",
        "Ligue em caso de urgência."
    ],
    "ministério público": [
        "O **Ministério Público (49 99188-2795)** atua na defesa jurídica e ações penais."
    ],
    "poder judiciário": [
        "O **Poder Judiciário (49 3521-8216)** garante direitos, julga casos e defere medidas protetivas."
    ],
    "oab por elas": [
        "A **OAB por Elas (49 3246-2090)** oferece assistência jurídica gratuita."
    ],
    "objetivos gerais": [
        "O objetivo do **Anjo Amigo** é apresentar a Rede de Proteção à Mulher em Fraiburgo."
    ],
    "objetivos específicos": [
        "Nossos objetivos incluem organizar a rede, qualificar o suporte e promover a conscientização."
    ],
    "apoio psicossocial": [
        "Você pode buscar **apoio psicossocial** no CREAS (49 3246-2826) ou CRAS (49 3256-3069)."
    ],
    "emergência": [
        "Em **emergência**, ligue imediatamente para 190, 192 ou 193."
    ],
    "botão do pânico": [
        "O **'botão do pânico'** está no app PMSC Cidadão para mulheres com medidas protetivas."
    ]
    # Você pode adicionar mais entradas conforme necessário
}
# Função para normalizar texto (sem acentos)
def normalize(text):
    return unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8").lower()

@app.post("/api/send")
async def send_message(msg: Message):
    user_input = normalize(msg.text)

    # Busca na base local
    for key in knowledge_base:
        if normalize(key) in user_input:
            return {"messages": knowledge_base[key]}

    # Se não encontrou, gera resposta com Gemini
    prompt = f"""
Você é um chatbot chamado "Anjo Amigo" focado em conscientização e combate à violência doméstica em Fraiburgo. Suas respostas devem ser **curtas, diretas e simular um comp>

Sua resposta deve ser um **JSON array de strings**. Cada string neste array será uma mensagem separada (um balão de fala).
Cada string (balão de fala) deve conter **no máximo uma expressão em negrito** (usando **texto** para negrito).
Se a informação for extensa ou precisar de mais de uma expressão em negrito, **divida-a em múltiplas strings no array JSON**.

Pergunta do usuário: {msg.text}
"""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"error": "Chave da API Gemini não encontrada. Verifique o arquivo .env."}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

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

    try:
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()

        candidates = result.get("candidates", [])
        if not candidates:
            return {"error": "Nenhuma resposta recebida da API Gemini."}

        content = candidates[0]["content"]["parts"][0]["text"]
        messages = json.loads(content)

        return {"messages": messages}

    except Exception as e:
        return {"error": f"Erro ao chamar ou processar resposta da API: {str(e)}"}
