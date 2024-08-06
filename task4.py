import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set your Hugging Face API key as an environment variable
os.environ['HUGGINGFACE_API_KEY'] = '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'

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2", use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained("gpt2", use_auth_token=True)

# Example text generation
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
