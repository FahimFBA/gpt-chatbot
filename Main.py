# Import openai
import openai

# api key
openai.api_key = "API_KEY"


def chat_with_chatbot(prompt):
    response = openai.ChatCompletion.create(
        # specify the model
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_chatbot(user_input)
        print("Chatbot ^^ : ", response)
