import chatbot_engine

bot = chatbot_engine.Chatbot()
print("=== Context-Aware Academic Chatbot ===")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")
    intent = bot.process_input(user_input)
    response = bot.get_response(intent)
    print("Bot:", response)

    if intent == "exit":
        break
