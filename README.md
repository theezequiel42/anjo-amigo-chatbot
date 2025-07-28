# 🤖 Anjo Amigo - Chatbot de Apoio à Mulher

Chatbot desenvolvido para apoiar mulheres em situação de violência doméstica na cidade de Fraiburgo, fornecendo informações sobre direitos, recursos disponíveis e orientações sobre onde buscar ajuda.

## 📋 Sobre o Projeto

O **Anjo Amigo** é uma ferramenta digital que visa oferecer suporte imediato e acessível para mulheres que enfrentam situações de violência doméstica. O chatbot fornece informações relevantes, orientações e direcionamentos para recursos locais de apoio.

## ✨ Funcionalidades

- 💬 Interface de chat intuitiva e acessível
- 🔍 Base de conhecimento especializada em violência doméstica
- 🏥 Informações sobre recursos locais em Fraiburgo
- ⚖️ Orientações sobre direitos da mulher
- 🆘 Direcionamento para canais de ajuda

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e rápido
- **Python 3.12** - Linguagem de programação
- **Google Gemini API** - Inteligência artificial para respostas
- **Uvicorn** - Servidor ASGI

### Frontend
- **HTML5** - Estrutura da página
- **CSS3** - Estilização
- **JavaScript** - Interatividade
- **Tailwind CSS** - Framework CSS
- **Lucide Icons** - Ícones

## 📁 Estrutura do Projeto

```
anjo-amigo-chatbot/
├── backend/
│   ├── knowledge/          # Base de conhecimento
│   ├── services/           # Serviços (Gemini API)
│   ├── utils/              # Utilitários
│   ├── config.py           # Configurações
│   ├── main.py             # Aplicação principal
│   ├── models.py           # Modelos de dados
│   ├── requirements.txt    # Dependências Python
│   └── routes.py           # Rotas da API
├── docker/
│   ├── Dockerfile          # Container Docker
│   └── .dockerignore       # Arquivos ignorados
└── frontend/
    ├── assets/             # Recursos estáticos
    ├── index.html          # Página principal
    ├── knowledgeBase.js     # Base de conhecimento JS
    ├── main.js             # Lógica principal
    └── styles.css          # Estilos personalizados
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.12+
- Chave da API do Google Gemini

### Configuração

1. **Clone o repositório:**
```bash
git clone https://github.com/theezequiel42/anjo-amigo-chatbot
cd anjo-amigo-chatbot
```

2. **Configure as variáveis de ambiente:**
```bash
# Crie um arquivo .env na pasta backend/
echo "GEMINI_API_KEY=sua_chave_aqui" > backend/.env
```

3. **Instale as dependências:**
```bash
cd backend
pip install -r requirements.txt
```

4. **Execute o servidor:**
```bash
uvicorn main:app --reload
```

5. **Acesse a aplicação:**
   - Backend: http://localhost:8000
   - Frontend: Abra `frontend/index.html` no navegador

### 🐳 Executar com Docker

```bash
# Na pasta raiz do projeto
docker build -f docker/Dockerfile -t anjo-amigo .
docker run -p 8000:8000 --env-file backend/.env anjo-amigo
```

## 🔧 Configuração da API

O projeto utiliza a API do Google Gemini. Para configurar:

1. Obtenha uma chave da API no [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Adicione a chave no arquivo `.env`:
```
GEMINI_API_KEY=sua_chave_da_api_gemini
```

## 📱 Como Usar

1. Acesse a interface web
2. Digite sua pergunta ou situação no campo de texto
3. O chatbot fornecerá informações relevantes e orientações
4. Para emergências, sempre procure ajuda imediata (190, 180)

## 📞 Contatos de Emergência

- **Polícia Militar:** 190
- **Central de Atendimento à Mulher:** 180
- **Disque Direitos Humanos:** 100

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

## ⚠️ Aviso Importante

Este chatbot é uma ferramenta de apoio e informação. Em situações de emergência, sempre procure ajuda imediata através dos canais oficiais (190, 180) ou dirija-se à delegacia mais próxima.