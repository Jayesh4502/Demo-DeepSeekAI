import requests
import json

url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

print("Type your prompt (type 'exit' to quit):")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Exiting...")
        break

    payload = {
        "model": "llama3",
        "prompt": user_prompt
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print("LLaMA3:", end=" ")
    for line in response.iter_lines():
        if line:
            print(json.loads(line)["response"], end="")

    print("\n")

