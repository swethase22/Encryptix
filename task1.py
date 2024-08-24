def response(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return("Hello, What can I do for you today?")
    elif "your name" in user_input:
        return ("My name is Elixer, I am a chatbot here to assist you :)")
    elif "how are you" in user_input:
        return("I'm doing great, how can I assist you today?")
    elif "bye" in user_input or "exit" in user_input:
        return("Thankyou and have a good day!")
    else:
        return("Sorry I dont know that one")
    

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    output = response(user_input)
    print(f"Chatbot: {output}")