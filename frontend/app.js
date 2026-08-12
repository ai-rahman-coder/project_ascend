const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const messages = document.getElementById("messages");

chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = messageInput.value.trim()

    if (!message) {
        return;
    }
 
    //show user's message
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", "user-message")
    messageElement.textContent = message;
    messages.appendChild(messageElement);

    //clear input
    messageInput.value = "";

    try{
        const response = await fetch("http://127.0.0.1:8000/chat/stream", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok){
            throw new Error("Request failed");
        }

        const aiMessage = document.createElement("div");
        aiMessage.classList.add("message", "ai-message");
        messages.appendChild(aiMessage);

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { value, done } = await reader.read()

            if (done) {
                break;
            }

            const chunk = decoder.decode(value, { stream: true});
            aiMessage.textContent += chunk;
        }
    }catch (error){
        console.error("Error", error)
    }
});