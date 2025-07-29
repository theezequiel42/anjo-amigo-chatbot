FROM python:3.12-slim

# Define o diretório padrão da aplicação
WORKDIR /app

# Copia apenas o requirements primeiro (para cache eficiente)
COPY backend/requirements.txt .

# Instala pip e dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o restante do backend
COPY backend/ .

# Expondo porta da API
EXPOSE 8000

# Comando padrão (pode ser sobrescrito no docker-compose.yml)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
