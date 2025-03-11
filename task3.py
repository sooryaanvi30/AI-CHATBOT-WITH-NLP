import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you?", "Hi there! How can I help?"]],
    [r"what is your name?", ["I'm a chatbot created with NLTK."]],
    [r"how are you?", ["I'm just a bot, but I'm functioning as expected!"]],
    [r"what can you do?", ["I can answer simple questions. Try asking about my name or greeting me."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def chatbot_interface():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run chatbot
if __name__ == "__main__":
    chatbot_interface()
