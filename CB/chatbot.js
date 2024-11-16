// Send user message to Rasa backend and display response
function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput === "") return;
  
    // Display user's message
    displayMessage(userInput, "user-message");
  
    // Clear the input field
    document.getElementById("user-input").value = "";
  
    // Send the message to the Rasa backend
    fetch("http://localhost:5005/webhooks/rest/webhook", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userInput }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data && data.length > 0) {
          // Display bot's response
          data.forEach((message) => {
            displayMessage(message.text, "bot-message");
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        displayMessage("Sorry, there was an error. Please try again.", "bot-message");
      });
  }
  
  // Function to display a message in the chat box
  function displayMessage(message, className) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${className}`;
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  