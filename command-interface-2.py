import requests
import json

url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Ask user for the model name once
model_name = input("Enter the model name (e.g., llama3, mistral): ").strip()

print(f"Using model: {model_name}")
print("Type your prompt (type 'exit' to quit):")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Exiting...")
        break

    payload = {
        "model": model_name,
        "prompt": user_prompt
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(f"{model_name}:", end=" ")
    for line in response.iter_lines():
        if line:
            print(json.loads(line)["response"], end="")

    print("\n")
