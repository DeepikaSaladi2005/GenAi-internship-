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
    total_tokens = response.usage['total_tokens']
    return message, total_tokens

def main():
    question = "How is the weather today?"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]
    
    # Generate the response
    response, total_tokens_used = generate_response(messages)
    
    print(f"Question: {question}")
    print(f"Chatbot: {response}")
    print(f"Total tokens used: {total_tokens_used}")

if __name__ == "__main__":
    main()

