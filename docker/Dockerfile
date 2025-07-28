FROM python:3.12-slim

WORKDIR /app

# Copia dependências
COPY backend/requirements.txt .

# Instala dependências com segurança (sem cache e com atualizações do sistema)
RUN apt-get update && apt-get upgrade -y && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia o restante do backend
COPY backend/ .

# Expõe a porta da API
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
