# set GROQ_API_KEY in the secrets

from groq import Groq


def start():
    # Create the Groq client
    client = Groq(api_key="GROQ_API_KEY_HERE")

    # Set the system prompt
    system_prompt = {
        "role": "system",
        "content": "You are a helpful assistant. You reply with very short answers.",
    }

    # Initialize the chat history
    chat_history = [system_prompt]

    while True:
        # Get user input from the console
        user_input = input("You: ")

        # Append the user input to the chat history
        chat_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=chat_history,
            max_tokens=100,
            temperature=1.2,
        )
        # Append the response to the chat history
        chat_history.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
        # Print the response
        print("Assistant:", response.choices[0].message.content)
