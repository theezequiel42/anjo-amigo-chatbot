/* main.js – Anjo Amigo v4 (voz + mute + ícones dinâmicos) */
window.addEventListener('DOMContentLoaded', () => {

    // === CONFIGURAÇÃO DO BACKEND ===
  const config = window.APP_CONFIG || {};
  const BASE_URL = config.USE_LOCAL_BACKEND ? config.LOCAL_URL : config.PROD_URL;
  // console.log("Backend ativo:", BASE_URL); // descomente para verificar o backend ativo

  /* ---------- elementos principais ---------- */
  const chatMessages   = document.getElementById('chat-messages');
  const userInput      = document.getElementById('user-input');
  const sendButton     = document.getElementById('send-button');
  const loadingIndicator = document.getElementById('loading-indicator');

  /* ---------- controle global ---------- */
  let isVoiceMuted = true;       // saída de voz desligada por padrão

  /* ---------- utilidades ---------- */
  function speak(text) {
    if (isVoiceMuted) return;
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'pt-BR';
    window.speechSynthesis.cancel();        // evita sobreposição
    window.speechSynthesis.speak(utter);
  }

  function displayMessage(text, sender) {
    const el = document.createElement('div');
    el.classList.add('message-bubble', sender === 'user' ? 'user-message' : 'bot-message');
    el.innerHTML = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    chatMessages.appendChild(el);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    setTimeout(() => el.classList.add('show'), 10);
    if (sender === 'bot') speak(el.textContent);     // lê (sem markdown)
  }

  async function displayMultipleMessages(msgs, sender, delay = 500) {
    for (const m of msgs) {
      displayMessage(m, sender);
      await new Promise(r => setTimeout(r, delay));
    }
  }

  /* ---------- boas-vindas ---------- */
  displayMultipleMessages([
    "Olá! Sou o **Anjo Amigo**, seu chatbot de apoio contra a violência doméstica em Fraiburgo.",
    "Posso te ajudar com informações sobre **leis**, seus direitos, tipos de violência e a rede de proteção.",
    "Como posso te ajudar hoje?"
  ], 'bot');

  /* ---------- envio de mensagem ---------- */
  async function sendMessage() {
    const userText = userInput.value.trim();
    if (!userText) return;

    displayMessage(userText, 'user');
    userInput.value = '';
    userInput.focus();
    loadingIndicator.style.display = 'block';
    sendButton.disabled = true;

    /* busca local na knowledgeBase */
    const normalized = userText.toLowerCase()
                               .normalize('NFD')
                               .replace(/[\u0300-\u036f]/g, '');

    for (const key in knowledgeBase) {
      const normKey = key.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
      if (normalized.includes(normKey)) {
        await displayMultipleMessages(knowledgeBase[key], 'bot');
        loadingIndicator.style.display = 'none';
        sendButton.disabled = false;
        return;
      }
    }

    /* fallback → FastAPI */
    try {
      const resp = await fetch(`${BASE_URL}/api/send`, {
        method : 'POST',
        headers: { 'Content-Type': 'application/json' },
        body   : JSON.stringify({ text: userText })
      });
      const result = await resp.json();
      if (Array.isArray(result.messages)) {
        await displayMultipleMessages(result.messages, 'bot');
      } else {
        displayMessage("Desculpe, recebi uma resposta inesperada. Por favor, tente novamente.", 'bot');
      }
    } catch (err) {
      console.error('Backend:', err);
      displayMessage("Ocorreu um erro ao tentar me conectar. Por favor, tente novamente mais tarde.", 'bot');
    } finally {
      loadingIndicator.style.display = 'none';
      sendButton.disabled = false;
    }
  }

  /* ---------- eventos de formulário ---------- */
  sendButton.addEventListener('click', sendMessage);
  userInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') { e.preventDefault(); sendMessage(); }
  });

  /* ---------- entrada por voz + ícone de microfone ---------- */
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = 'pt-BR';
    recognition.interimResults = false;

    /* helper – retorna SVG do microfone, conforme estado */
    const micSvg = (listening = false) => listening
      ? `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
               fill="currentColor">
           <path d="M12 1a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3Z"/>
           <path d="M5 10v0a7 7 0 0 0 14 0v0"/>
           <line x1="12" y1="19" x2="12" y2="23"></line>
           <line x1="8"  y1="23" x2="16" y2="23"></line>
         </svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
               fill="none" stroke="currentColor" stroke-width="2"
               stroke-linecap="round" stroke-linejoin="round">
           <path d="M12 1a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3Z"></path>
           <path d="M19 10a7 7 0 0 1-14 0"></path>
           <line x1="12" x2="12" y1="19" y2="23"></line>
           <line x1="8"  x2="16" y1="23" y2="23"></line>
         </svg>`;

    /* botão de microfone */
    const micBtn = document.createElement('button');
    micBtn.type = 'button';
    micBtn.className = 'icon-btn';
    micBtn.innerHTML = micSvg(false);
    sendButton.insertAdjacentElement('afterend', micBtn);

    micBtn.addEventListener('click', () => recognition.start());

    /* muda estado visual durante a escuta */
    recognition.addEventListener('start', () => {
      micBtn.classList.add('listening');
      micBtn.innerHTML = micSvg(true);
    });
    recognition.addEventListener('end', () => {
      micBtn.classList.remove('listening');
      micBtn.innerHTML = micSvg(false);
    });

    recognition.addEventListener('result', e => {
      const transcript = e.results[0][0].transcript;
      userInput.value = transcript;
      sendMessage();
    });

    recognition.addEventListener('error', e => {
      console.error('Voz:', e.error);
      displayMessage("Desculpe, não consegui entender o que você disse.", 'bot');
    });
  } else {
    console.warn('Reconhecimento de voz não suportado neste navegador.');
  }

  /* ---------- botão Mute / Un-mute ---------- */
  const muteBtn = document.createElement('button');
  muteBtn.type = 'button';
  muteBtn.className = 'icon-btn';
  muteBtn.setAttribute('aria-pressed', 'false');
  muteBtn.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
         viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
      <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
      <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
    </svg>`;
  sendButton.insertAdjacentElement('afterend', muteBtn);

  muteBtn.addEventListener('click', () => {
    isVoiceMuted = !isVoiceMuted;
    muteBtn.setAttribute('aria-pressed', String(isVoiceMuted));
    muteBtn.classList.toggle('muted', isVoiceMuted);
    /* troca ícone */
    muteBtn.querySelector('svg').innerHTML = isVoiceMuted
      ? `<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
         <line x1="23" x2="17" y1="9" y2="15"></line>
         <line x1="17" x2="23" y1="9" y2="15"></line>`
      : `<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
         <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
         <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>`;
  });
});
