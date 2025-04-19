import requests
import json

url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Get the first model name and prompt from user
first_model = input("Enter the first model name (e.g., llama3, mistral): ").strip()
initial_prompt = input(f"Enter your prompt for {first_model}: ").strip()

# Step 1: Send to the first model
payload1 = {
    "model": first_model,
    "prompt": initial_prompt
}

response1 = requests.post(url, data=json.dumps(payload1), headers=headers)

print(f"\nResponse from {first_model}:")
model1_output = ""
for line in response1.iter_lines():
    if line:
        part = json.loads(line)["response"]
        model1_output += part
        print(part, end="")
print("\n")

# Step 2: Send first model's output to gemma:3b
second_model = "gemma3:1b"
payload2 = {
    "model": second_model,
    "prompt": model1_output
}

print(f"\nSending output from {first_model} to {second_model}...")

response2 = requests.post(url, data=json.dumps(payload2), headers=headers)

print(f"\nResponse from {second_model}:")
got_response = False
for line in response2.iter_lines():
    if line:
        try:
            data = json.loads(line)
            print(data.get("response", ""), end="")
            got_response = True
        except json.JSONDecodeError:
            print("\n[Warning] Could not parse line as JSON:\n", line.decode('utf-8'))

if not got_response:
    print("[!] No response was received from gemma:3b.")
