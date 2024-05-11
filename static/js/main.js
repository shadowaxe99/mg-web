// Initialize the conversation UI
function initConversation() {
  document.querySelector('#send-message-button').addEventListener('click', sendMessage);
}

// Display a message in the conversation
function displayMessage(sender, text) {
  const messageContainer = document.createElement('div');
  messageContainer.classList.add(sender === 'fan' ? 'fan-message' : 'ai-influencer-message');

  const messageText = document.createElement('p');
  messageText.textContent = text;

  messageContainer.appendChild(messageText);
  document.querySelector('#conversation-container').appendChild(messageContainer);
}

// Handle sending messages
function sendMessage() {
  const messageInput = document.querySelector('#message-input');
  const messageText = messageInput.value.trim();

  if (messageText) {
    displayMessage('fan', messageText);
    messageInput.value = '';

    // Simulate AI response
    fetch('/api/conversation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: messageText })
    })
    .then(response => response.json())
    .then(data => {
      if (data && data.reply) {
        displayMessage('ai_influencer', data.reply);
      }
    })
    .catch(error => console.error('Error during conversation:', error));
  }
}

// Handle feature purchase
function purchaseFeature(featureId) {
  // Placeholder for purchasing logic
  console.log(`Feature ${featureId} purchased!`);
  // Emit a monetization event
  handleMonetizationEvent('FEATURE_PURCHASE', featureId);
}

// Handle subscription to a service
function subscribeToService(serviceId) {
  // Placeholder for subscription logic
  console.log(`Subscribed to service ${serviceId}!`);
  // Emit a monetization event
  handleMonetizationEvent('SERVICE_SUBSCRIPTION', serviceId);
}

// Handle monetization events
function handleMonetizationEvent(eventType, detail) {
  // Placeholder for handling different types of monetization events
  console.log(`Monetization event: ${eventType} with detail: ${detail}`);
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
  initConversation();
});