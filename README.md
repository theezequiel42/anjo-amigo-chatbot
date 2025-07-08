# Anjo Amigo - AI-Powered Domestic Violence Support Chatbot for Fraiburgo

Anjo Amigo is a specialized chatbot designed to provide immediate, accessible information about domestic violence resources and support services in Fraiburgo, Brazil. 
The system combines a local knowledge base with AI-powered responses to deliver accurate, context-aware information about violence prevention, legal rights, and available support networks.

The chatbot serves as a digital gateway to Fraiburgo's Women's Protection Network, offering information about different types of domestic violence, emergency contacts, and local support services. 
It features a user-friendly interface that provides real-time responses through an intuitive chat interface, making critical information accessible to those who need it most.

## Repository Structure
```
.
├── index.html          # Frontend interface with chat UI and client-side logic
└── main.py            # FastAPI backend server with knowledge base and Gemini AI integration
```

## Usage Instructions
### Prerequisites
- Python 3.7+
- FastAPI
- Python-dotenv
- Requests library
- Web browser with JavaScript enabled
- Gemini API key

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd anjo-amigo
```

2. Install Python dependencies:
```bash
pip install fastapi uvicorn python-dotenv requests
```

3. Create a `.env` file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here
```

### Quick Start

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open `index.html` in a web browser

3. Begin interacting with the chatbot by typing questions about domestic violence resources in Fraiburgo

### More Detailed Examples

1. Asking about types of violence:
```
User: "What is physical violence?"
Bot: "Physical violence involves bodily aggression.
     In emergencies, call 190 (Military Police)."
```

2. Getting emergency contacts:
```
User: "How can I report domestic violence?"
Bot: "To report, call 190 (Military Police).
     You can also file a police report at the Civil Police - Sala Lilás."
```

### Troubleshooting

Common Issues:
1. API Key Not Found
   - Error: "Gemini API key not found"
   - Solution: Ensure `.env` file exists with valid `GEMINI_API_KEY`

2. CORS Issues
   - Error: Cross-Origin Request Blocked
   - Solution: Check CORS middleware configuration in main.py

3. Server Connection Issues
   - Error: Cannot connect to server
   - Solution: Verify uvicorn is running and port is available

## Data Flow
The chatbot processes user queries through a two-stage response system, first checking a local knowledge base before falling back to AI-generated responses.

```ascii
User Input -> [Frontend] -> HTTP Request -> [Backend] 
                                             |
                                      Check Local KB
                                             |
                                     [If not found]
                                             |
                                      Query Gemini AI
                                             |
                           JSON Response -> [Frontend] -> Display
```

Key Component Interactions:
1. Frontend sends user messages to backend via POST /api/send
2. Backend first checks local knowledge base for matches
3. If no match found, query is processed by Gemini AI
4. Responses are formatted as JSON arrays of strings
5. Frontend displays messages with animation effects
6. Messages support Markdown-style bold text formatting
7. System maintains conversation context and flow