def chatbot():
    print("🤖 AI Chatbot")
    print("Type 'bye' to end the chat.\n")

    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I'm doing great! What about you?",
        "your name": "I'm an AI Chatbot created using Python.",
        "what can you do": "I can answer simple questions and chat with you.",
        "thank you": "You're welcome!",
        "thanks": "Happy to help!",
    }

    while True:
        user = input("You: ").lower()

        if user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        found = False
        for key in responses:
            if key in user:
                print("Bot:", responses[key])
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't understand that. Please ask something else.")

chatbot()