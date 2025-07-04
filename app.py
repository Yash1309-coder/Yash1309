import google.generativeai as genai

API_KEY = "AIzaSyBeMKdiOS1dM8WzLbsBv6GWhp8C5hF7DKU"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini ! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:" , response.text)