# 🤖 Anjo Amigo – Chatbot de Apoio à Mulher

**Anjo Amigo** é um chatbot desenvolvido para apoiar mulheres em situação de **violência doméstica** na cidade de **Fraiburgo**, fornecendo informações confiáveis sobre seus **direitos**, a **rede de proteção local** e **orientações úteis** para quem precisa de ajuda.

---

## 📌 Visão Geral

Esta ferramenta digital busca promover o acolhimento, a informação e a conscientização. O chatbot atua como um canal acessível de apoio emocional e orientação, utilizando inteligência artificial para enriquecer a experiência de conversa.

---

## ✨ Funcionalidades

- 💬 Interface de chat leve, intuitiva e acessível
- 🧐 Base de conhecimento especializada em violência doméstica
- 📍 Informações sobre recursos locais de Fraiburgo
- ⚖️ Orientações claras sobre os direitos das mulheres
- 🤝 Direcionamento para canais de denúncia e apoio
- 🗣️ Entrada e saída por voz (suporte a browsers compatíveis)
- 🖼️ Ícones dinâmicos com feedback visual

---

## 🛠️ Tecnologias Utilizadas

### 🔙 Backend

- [FastAPI](https://fastapi.tiangolo.com/) – Web framework moderno
- [Python 3.12](https://www.python.org/)
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI rápido
- [Google Gemini API](https://makersuite.google.com/) – Geração de conteúdo com IA

### 🔜 Frontend

- HTML5 + JavaScript puro (sem frameworks)
- [Tailwind CSS](https://tailwindcss.com/) – Utilitários de estilização
- [Lucide Icons](https://lucide.dev/) – Ícones de código aberto

---

## 📁 Estrutura do Projeto

```
anjo-amigo-chatbot/
├── backend/
│   ├── knowledge/          # Base de conhecimento local
│   ├── services/           # Integração com IA (Gemini)
│   ├── utils/              # Funções auxiliares
│   ├── config.py           # Carregamento de variáveis de ambiente
│   ├── main.py             # Inicialização da API FastAPI
│   ├── models.py           # Modelos Pydantic
│   ├── routes.py           # Rotas da API
│   ├── requirements.txt    # Dependências Python
│   └── .env                # Chave da API Gemini
├── docker/
│   ├── Dockerfile          # Container do backend
│   └── .dockerignore       # Arquivos ignorados na imagem
└── frontend/
    ├── assets/             # Imagens, ícones e SVGs
    ├── index.html          # Interface web principal
    ├── main.js             # Lógica do chatbot
    ├── knowledgeBase.js    # Base de conhecimento em JS
    └── styles.css          # Estilos customizados
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.12 ou superior
- Chave da API Gemini (veja abaixo)

### Passos

1. **Clone o repositório**

```bash
git clone https://github.com/theezequiel42/anjo-amigo-chatbot
cd anjo-amigo-chatbot
```

2. **Configure a chave da API Gemini**

```bash
echo "GEMINI_API_KEY=sua_chave_aqui" > backend/.env
```

3. **Instale as dependências**

```bash
cd backend
pip install -r requirements.txt
```

4. **Inicie o backend**

```bash
uvicorn main:app --reload
```

5. **Acesse o frontend**

Abra `frontend/index.html` no navegador ou sirva com:

```bash
cd frontend
python -m http.server 5500
```

---

## 🐳 Executar com Docker

### Build da imagem:

```bash
docker build -f docker/Dockerfile -t anjo-amigo .
```

### Rodar o container:

```bash
docker run -p 8000:8000 --env-file backend/.env anjo-amigo
```

Ou com `docker-compose`:

```bash
docker-compose up --build
```

> O backend estará acessível em: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Configuração da API Gemini

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Gere uma nova chave de API
3. Salve no arquivo `backend/.env`:

```env
GEMINI_API_KEY=sua_chave_da_api_gemini
```

---

## 🤖 Modo de Teste Local com Frontend

O `frontend/env.js` permite alternar entre o backend local e o da VPS:

```js
window.APP_CONFIG = {
  USE_LOCAL_BACKEND: true,
  LOCAL_URL: "http://localhost:8000",
  PROD_URL: "https://anjoamigo.seudominio.com"
};
```

---

## 📱 Como Usar

1. Digite sua dúvida ou situação no campo de mensagem
2. O chatbot responderá com informações úteis
3. Se desejar, ative ou desative a voz
4. Em caso de emergência, ligue para os canais oficiais

---

## 📞 Contatos de Emergência

- 📱 **Polícia Militar:** 190
- ☎️ **Central de Atendimento à Mulher:** 180
- 🧒 **Disque Direitos Humanos:** 100

---

## ⚠️ Aviso Importante

> Este chatbot é uma ferramenta de apoio informativo e **não substitui canais de emergência**.\
> Se estiver em perigo, procure ajuda imediata ligando para 190 ou 180, ou vá até uma delegacia especializada.

---


