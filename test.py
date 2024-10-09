import json
import requests


url = "http://localhost:5000/process"

headers = {
    "Content-Type": "application/json"
}

user_request = input("Введите ваше сообщение: ")

while user_request != "exit":
    response = requests.post(url=url, data=json.dumps({"prompt": user_request}), headers=headers).json()

    error_status = response.get("error", None)
    if error_status is None:
        print("meta-llama/Meta-Llama-3-8B-Instruct (Hugging Face API):\n" + response["hugging_face_response"])
        print("GPT-4.2 (RAPID API):\n" + response["gpt_response"])
    else:
        print("ERROR:\n" + error_status)
    
    user_request = input("Введите ваше сообщение: ")