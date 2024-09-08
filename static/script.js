// Loading Animation
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const loaderContainer = document.getElementById("loader-container");
    const chatHistory = document.getElementById('chat-history');
    const promptInput = document.getElementById('prompt-input');

    form.addEventListener("submit", function(e) {
        e.preventDefault();  // Prevent the form from refreshing the page
        const userMessage = promptInput.value.trim();
        
        if (userMessage === "") return;

        // Show the user's message in chat
        const userEntry = document.createElement('div');
        userEntry.classList.add('chat-entry', 'user');
        userEntry.innerHTML = `<div class="bubble"><strong>You:</strong><p>${userMessage}</p></div>`;
        chatHistory.appendChild(userEntry);

        // Clear the input field
        promptInput.value = '';

        // Show loader
        loaderContainer.style.visibility = "visible"; 

        // Simulate generating response (replace this with actual AI response)
        setTimeout(function() {
            loaderContainer.style.visibility = "hidden"; // Hide loader
            const assistantMessage = "Here is your answer to that!";
            
            // Show the assistant's message in chat
            const assistantEntry = document.createElement('div');
            assistantEntry.classList.add('chat-entry', 'assistant');
            assistantEntry.innerHTML = `<div class="bubble"><strong>Homework Tutor:</strong><p>${assistantMessage}</p></div>`;
            chatHistory.appendChild(assistantEntry);
            
            // Scroll to the bottom of the chat
            chatHistory.scrollTop = chatHistory.scrollHeight;
        }, 3000);  // Simulate delay
    });

    // Clear button
    document.getElementById('clear-button').addEventListener('click', function() {
        chatHistory.innerHTML = '';  // Clear chat history
    });
});
