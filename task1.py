import streamlit as st
from datetime import datetime

def response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello, What can I do for you today?"
    elif "your name" in user_input:
        return "My name is Elixer, I am a chatbot here to assist you :)"
    elif "how are you" in user_input:
        return "I'm doing great, how can I assist you today?"
    elif "bye" in user_input or "exit" in user_input:
        return "Thank you and have a good day!"
    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    elif "weather" in user_input:
        return "I don't have access to weather data, but I hope it's sunny wherever you are!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "thanks" in user_input:
        return "You are welcome. I'm always here to assist you. Let me know if there is anything else."
    else:
        return "Sorry, I don't know that one."

def main():
    st.title("ELIXER")
    st.write("Hello! I'm Elixer, your friendly chatbot. How can I assist you today?")

    user_input = st.text_input("You: ", "")
    
    if st.button("Send"):
        if user_input.lower() in ["exit", "quit"]:
            st.write("Chatbot: Goodbye! Have a good day :)")
        else:
            output = response(user_input)
            st.write(f"Chatbot: {output}")

if __name__ == "__main__":
    main()
