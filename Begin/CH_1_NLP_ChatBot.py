# This imports the textblob class from the Textblob module
from textblob import TextBlob

# Defining the chatBot class for interaction.
class ChatBot:
    def __init__(self):
        # Define intents and their corresponding responses based on keywords
        self.intents = {
            "hours": {
                "keywords": ["hours", "open", "close"],
                "response": "We are open from 9 AM to 5 PM, Monday to Friday."
            },
            "return": {
                "keywords": ["refund", "money back", "return"],
                "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
            }
        }
    # Analyzing the sentiment of the user's message
    def get_response(self, message):
        # Convert the message to lowercase for consistent keyword matching
        message = message.lower()
        for intent_data in self.intents.values():
            # Check if the message contains any keywords associated with defined intents
            if any(word in message for word in intent_data["keywords"]):
                return intent_data["response"]
            
        # Analyze the sentiment of the message using TextBlob
        sentiment = TextBlob(message).sentiment.polarity

        # Return a response based on the sentiment score
        return ("That's great to hear!" if sentiment > 0 else
                "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
                "I see. Can you tell me more about that?")

    def chat(self):
        # Greet the user and prompt for input
        print("ChatBot: Hi, how can I help you today?")
        # Continuously prompt the user for input until they choose to exit
        while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
            print(f"\nChatBot: {self.get_response(user_message)}")
            # Thank the user for chatting when they exit
        print("ChatBot: Thank you for chatting. Have a great day!")
  

if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    ChatBot().chat()
