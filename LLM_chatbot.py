# Simple LLM powered Chatbot

# I got the Gemini API key to use the Gemini Flash 2.0

# import getpass
import google.generativeai as genai # type: ignore
import os


api_key = os.getenv("GOOGLE_API_KEY")
print("DEBUG: API key length", len(api_key) if api_key else "NOT FOUND")

if not api_key:
    raise ValueError("Environment variable Google API key is not set!")

# configuring the Generative AI client
genai.configure(api_key=api_key)


# Initialize the Gemini chat model through loading and start the session# 
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()


# defining the chat function
def chat_with_gemini(user_input):
    response = chat.send_message(user_input)
    return response.text


# chat with the Bot
print("I am Gemini ChatBot: Are you ready to chat with me!")

while True:
    user_input = input('Please Type:')
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: GoodBye")
        break
    reply = chat_with_gemini(user_input)
    print("Bot:", reply)
