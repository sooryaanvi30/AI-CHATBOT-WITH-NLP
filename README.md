# AI-CHATBOT-WITH-NLP
COMPANY: CODTECH IT SOLUTIONS

NAME: P SOORYA SHENOY

INTERN ID: CT12ONS

DOMAIN: PYTHON PROGRAMMING

DURATION: 8 WEEKS

MENTOR: NEELA SANTHOSH

DESCRIPTION: This Python script implements a simple chatbot using the nltk library. It defines a set of predefined user input patterns and corresponding responses using the Chat module from nltk.chat.util. The chatbot can recognize greetings, answer basic questions about itself, and respond to farewells. The chatbot_interface() function provides an interactive terminal-based conversation, where user inputs are matched against the predefined patterns. The chatbot continues running until the user types "bye," "exit," or "quit." The script showcases basic natural language processing (NLP) techniques for rule-based chatbot development using Python.
Importing Necessary Modules:
nltk: A popular NLP library.
Chat and reflections from nltk.chat.util: Used for rule-based chatbot interaction.

Defining Patterns and Responses:
The pairs list contains tuples of regex patterns and their corresponding responses.
The chatbot recognizes greetings (hi, hello, hey), questions (what is your name?, how are you?), and farewells (bye, goodbye).
Each pattern is mapped to a list of possible responses.

Creating the Chatbot Instance:
Chat(pairs, reflections): Initializes the chatbot using predefined patterns.
reflections: A dictionary that automatically replaces pronouns (e.g., "I am" → "You are").

Chatbot Interaction Function (chatbot_interface()):
Runs a loop to continuously take user input.
If the user types "bye", "exit", or "quit", the chatbot exits.
Otherwise, it responds using the respond() method of Chat.

Running the Chatbot:
The script runs the chatbot if executed directly (if __name__ == "__main__":).
This ensures interactive user engagement through the console.

This chatbot interacts with users through text-based input and output in a console environment. The user provides input by typing messages, which are processed using predefined pattern-matching rules. The chatbot recognizes basic greetings such as "hi," "hello," and "hey," as well as simple queries like "what is your name?" or "how are you?" using regular expressions. If the input matches a pattern, the chatbot selects an appropriate response from a predefined list. If the user enters an exit command like "bye," "exit," or "quit," the chatbot acknowledges the farewell and terminates the conversation. The chatbot's responses are displayed in real-time, making the interaction feel natural and conversational. However, if the input does not match any predefined pattern, the chatbot may not provide a meaningful response. The reflections dictionary allows for dynamic word replacements, ensuring that responses sound more personalized. The chatbot runs in a continuous loop until an exit command is detected, making it a simple yet effective example of a rule-based chatbot using the nltk library.

OUTPUT:
![image](https://github.com/user-attachments/assets/8e6e119f-4459-413d-965a-1bfe802f9746)






