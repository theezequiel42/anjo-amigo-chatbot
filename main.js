window.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Exibe uma única mensagem com formatação e animação
    function displayMessage(text, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message-bubble', sender === 'user' ? 'user-message' : 'bot-message');
        messageElement.innerHTML = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        setTimeout(() => {
            messageElement.classList.add('show');
        }, 10);
    }

    // Exibe múltiplas mensagens em sequência com delay
    async function displayMultipleMessages(messages, sender, delay = 500) {
        for (const msg of messages) {
            displayMessage(msg, sender);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    }

    // Exibe mensagens de boas-vindas ao carregar a página
    displayMultipleMessages([
        "Olá! Sou o **Anjo Amigo**, seu chatbot de apoio contra a violência doméstica em Fraiburgo.",
        "Posso te ajudar com informações sobre **leis**, seus direitos, tipos de violência e a rede de proteção.",
        "Como posso te ajudar hoje?"
    ], 'bot');

    // Função principal de envio de mensagens
    async function sendMessage() {
        const userText = userInput.value.trim();
        if (!userText) return;

        // Feedback visual imediato
        displayMessage(userText, 'user');
        userInput.value = '';
        userInput.focus();
        loadingIndicator.style.display = 'block';
        sendButton.disabled = true;

        const normalizedQuery = userText
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");

        let found = false;

        for (const key in knowledgeBase) {
            const normalizedKey = key
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "");
            if (normalizedQuery.includes(normalizedKey)) {
                await displayMultipleMessages(knowledgeBase[key], 'bot');
                found = true;
                break;
            }
        }

        if (found) {
            loadingIndicator.style.display = 'none';
            sendButton.disabled = false;
            return;
        }

        // Caso não esteja na base local, consulta API externa
        try {
            const response = await fetch("http://82.29.61.210:8000/api/send", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: userText })
            });

            const result = await response.json();

            if (result.messages && Array.isArray(result.messages)) {
                await displayMultipleMessages(result.messages, 'bot');
            } else {
                displayMessage("Desculpe, recebi uma resposta inesperada. Por favor, tente novamente.", 'bot');
            }

        } catch (error) {
            console.error("Erro ao chamar o backend:", error);
            displayMessage("Ocorreu um erro ao tentar me conectar. Por favor, tente novamente mais tarde.", 'bot');

        } finally {
            loadingIndicator.style.display = 'none';
            sendButton.disabled = false;
        }
    }

    // Eventos
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });
});
