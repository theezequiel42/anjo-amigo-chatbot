# Anjo Amigo - AI-Powered Domestic Violence Support Chatbot for Fraiburgo

Anjo Amigo is a specialized chatbot designed to provide immediate support and information about domestic violence resources in Fraiburgo, Brazil. The application offers an accessible, user-friendly interface that connects users with local support services, legal information, and emergency contacts while maintaining privacy and providing real-time assistance.

The chatbot combines a local knowledge base with AI-powered responses through the Gemini API to deliver accurate, context-aware information about domestic violence support services. Key features include text-to-speech capabilities, voice input support, multilingual accessibility, and real-time responses covering topics from emergency contacts to legal rights under the Maria da Penha Law. The system integrates with local support networks including CREAS, CRAS, law enforcement, and healthcare providers to ensure comprehensive assistance.

## Repository Structure
```
.
├── index.html          # Main HTML interface with chat UI components
├── knowledgeBase.js    # Local database of support services and violence types
├── main.js            # Core JavaScript for chat functionality and UI interactions
├── main.py            # FastAPI backend with Gemini API integration
└── styles.css         # CSS styling for chat interface and animations
```

## Usage Instructions
### Prerequisites
- Python 3.7+ for backend server
- Modern web browser with JavaScript enabled
- Internet connection for API access
- Gemini API key (for backend services)

### Installation

#### Backend Setup
```bash
# Install Python dependencies
pip install fastapi uvicorn python-dotenv requests

# Set up environment variables
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Start the backend server
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### Frontend Setup
```bash
# Serve the frontend files using any HTTP server
# Example using Python's built-in server:
python -m http.server 8080
```

### Quick Start
1. Access the application through your web browser at `http://localhost:8080`
2. The chatbot will display welcome messages explaining available services
3. Type your question or use the voice input button to interact
4. Receive immediate responses with relevant information and local resources

### More Detailed Examples

#### Text Input Example
```javascript
// Ask about domestic violence types
User: "What are the types of domestic violence?"
Bot: [
    "There are several types of domestic violence:",
    "**Physical violence** includes bodily harm",
    "**Psychological violence** involves emotional damage",
    "**Sexual violence** covers unwanted sexual acts",
    "**Patrimonial violence** involves property damage or theft",
    "**Moral violence** includes defamation and slander"
]
```

#### Voice Input Usage
1. Click the microphone icon
2. Speak your question clearly
3. The system will automatically transcribe and process your query
4. Receive both text and voice responses

### Troubleshooting

#### Common Issues
1. Backend Connection Errors
   - Error: "Unable to connect to backend"
   - Solution: Verify the backend server is running and check CORS settings
   - Debug: Check console logs for specific error messages

2. Voice Recognition Issues
   - Error: "Speech recognition not supported"
   - Solution: Use a supported browser (Chrome, Edge, Safari)
   - Check microphone permissions in browser settings

3. API Response Failures
   - Error: "Unexpected response from API"
   - Solution: Verify Gemini API key and quota
   - Check network connectivity and API status

## Data Flow
The Anjo Amigo chatbot processes user queries through a multi-stage pipeline, combining local knowledge base lookups with AI-powered responses for comprehensive support.

```ascii
User Input → Local KB Check → [Match Found] → Direct Response
                           → [No Match] → Gemini API → AI Response
                                      → Text-to-Speech Output
```

Key Component Interactions:
- Frontend captures user input via text or voice
- Local knowledge base provides immediate responses for known topics
- FastAPI backend processes complex queries through Gemini API
- Text-to-speech engine converts responses for accessibility
- Response formatting adds markdown emphasis for important information
- Error handling ensures graceful fallbacks at each step
- Real-time updates maintain conversation flow