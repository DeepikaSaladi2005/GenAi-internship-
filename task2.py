import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

def generate_design(prompt, model="claude-v1", role="You are an expert in interior designing."):
   
    client = anthropic.Client(api_key=anthropic_api_key)
    response = client.completions.create(
        model=model,
        prompt=f"{role}\n{prompt}",
        max_tokens=800,
        temperature=0.0
    )
    
    return response.completion


# Example usage
prompt = """You are an expert in interior designing.
Solve the following problem:
I have an area. Please design the house with a triple bedroom, a living hall with a kitchen and a storeroom. One of the bedrooms is for kids. The house also needs a balcony and a playing area."""

model = "claude-v1"
role = "You are an expert in interior designing."

result = generate_design(prompt, model, role)

# Print model name, prompt, and role line by line
print("Model name:", model)
print("Prompt:")
print(prompt)
print("Role:", role)
print("Generated Design:")
print(result)


