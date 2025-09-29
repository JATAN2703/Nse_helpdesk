


const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null;
const API_KEY = "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";
const inputInitHeight = chatInput.scrollHeight;
let keywordResponses = {};

const loadResponses = async () => {
    try {
        const response = await fetch("responses.json");
        keywordResponses = await response.json();
    } catch (error) {
        console.error("Failed to load responses from the JSON file: " + error.message);
    }
};

loadResponses();

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi;
};

const addShowResponseFunctionality = (messageElement, fullResponse) => {
    messageElement.style.display = "none";

    const showResponseButton = document.createElement("button");
    showResponseButton.textContent = "Show Response";
    showResponseButton.classList.add("show-response-button");

    messageElement.parentNode.insertBefore(showResponseButton, messageElement.nextSibling);

    showResponseButton.addEventListener("click", () => {
        showResponseButton.style.display = "none";
        messageElement.style.display = "block";
    });

    messageElement.textContent = fullResponse;
};

const generateResponse = (chatElement) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = chatElement.querySelector("p");

    const predefinedResponse = keywordResponses[userMessage];
    if (predefinedResponse) {
        addShowResponseFunctionality(messageElement, predefinedResponse);
        chatbox.scrollTo(0, chatbox.scrollHeight);
    } else {
        const requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`,
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: userMessage }],
            }),
        };
        fetch(API_URL, requestOptions)
            .then((res) => res.json())
            .then((data) => {
                const responseData = data.choices[0].message.content.trim();
                if (responseData === "Oops!") {
                    const fallbackResponse = keywordResponses["fallback"];
                    addShowResponseFunctionality(messageElement, fallbackResponse);
                } else {
                    messageElement.textContent = responseData;
                }
            })
            .catch(() => {
                messageElement.classList.add("error");
                messageElement.textContent =  "Oops!, I couldn't find a specific response to your query. If you have any other questions or need assistance with NSE topics, feel free to ask."
            })
            .finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
    }
};


const handleChat = () => {
    userMessage = chatInput.value.trim().toLowerCase();
    if (!userMessage) return;

    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    for (const keyword in keywordResponses) {
        if (userMessage.includes(keyword.toLowerCase())) {
            const keywordResponse = keywordResponses[keyword];
            const incomingChatLi = createChatLi(keywordResponse, "incoming");
            chatbox.appendChild(incomingChatLi);
            chatbox.scrollTo(0, chatbox.scrollHeight);
            return;
        }
    }

    const incomingChatLi = createChatLi("Thinking....", "incoming");
    chatbox.appendChild(incomingChatLi);
    chatbox.scrollTo(0, chatbox.scrollHeight);
    generateResponse(incomingChatLi);
};

chatInput.addEventListener("input", () => {
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));





