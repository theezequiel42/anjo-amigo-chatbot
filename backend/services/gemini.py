import requests
import json
import re
from config import get_gemini_api_key

GEMINI_MODEL = "gemini-2.0-flash"  # Ou "gemini-2.0-pro" se preferir

def generate_response_with_gemini(user_input: str):
    prompt = f"""
Você é um chatbot chamado "Anjo Amigo", focado em conscientização e combate à violência doméstica em Fraiburgo.

### Diretrizes:
- Suas respostas devem ser **curtas, diretas e empáticas**, como um companheiro de conversa.
- NÃO use markdown nem blocos de código (ex: ```json).
- NÃO use cabeçalhos, títulos ou emojis.
- Sua resposta deve ser **apenas um array JSON de strings** (sem envolver em markdown).
- Cada string no array representa um **balão de fala separado**.
- Cada balão pode conter **no máximo uma expressão em negrito**, usando **duplo asterisco**, como em **importante**.
- Se for necessário transmitir mais de uma ideia ou mais de um termo em negrito, **divida em múltiplos balões** (strings separadas).

### Contexto:
- Você não pode chamar ajuda nem acessar serviços externos.
- Use linguagem acessível, sem termos técnicos.
- Sempre que possível, utilize exemplos práticos.

### Entrada do usuário:
{user_input}
""".strip()

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={get_gemini_api_key()}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()

        result = response.json()
        candidates = result.get("candidates", [])
        if not candidates:
            return ["Desculpe, não consegui gerar uma resposta no momento."]

        text_output = candidates[0]["content"]["parts"][0]["text"].strip()

        # Remove blocos markdown ```json ... ```
        if text_output.startswith("```"):
            text_output = re.sub(r"^```(?:json)?\n|\n```$", "", text_output.strip())

        # Tenta converter em array JSON válido
        try:
            parsed = json.loads(text_output)
            if isinstance(parsed, list) and all(isinstance(msg, str) for msg in parsed):
                return parsed
            else:
                return [text_output]  # Se não for lista de strings, retorna como texto simples
        except json.JSONDecodeError:
            return [text_output]  # Se não conseguir fazer parse, retorna texto puro

    except requests.exceptions.HTTPError as http_err:
        print(f"[GEMINI] HTTP error: {http_err}")
        return [f"Erro ao conectar com o Gemini: {http_err}"]
    except requests.exceptions.RequestException as err:
        print(f"[GEMINI] Request exception: {err}")
        return ["Serviço temporariamente indisponível. Por favor, tente novamente mais tarde."]
    except Exception as e:
        print(f"[GEMINI] Erro inesperado: {e}")
        return ["Ocorreu um erro inesperado."]
