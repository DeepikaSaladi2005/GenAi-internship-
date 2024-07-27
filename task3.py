import openai

openai.api_key = "API key"
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].message['content'].strip()
    return message

def chat():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        messages.append({"role": "user", "content": user_input})
        
    
        response = generate_response(messages)
  
        messages.append({"role": "assistant", "content": response})
        
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
