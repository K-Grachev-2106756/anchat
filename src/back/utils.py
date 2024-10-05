import requests

from config import BASE_PROMPT, HF, GPT


# Функция для отправки запроса на Hugging Face
def send_to_hugging_face(request):
    result = []

    HF["params"]["messages"] = [
        {"role": "system", "content": BASE_PROMPT}, {"role": "user", "content": request}
    ]

    for message in HF["client"].chat_completion(**HF["params"]):
        result.append(message.choices[0].delta.content)
    
    return "".join(result)


# Функция для отправки запроса на gpt через rapid-api
def send_to_gpt(request):
    GPT["params"]["messages"] = [
        {"role": "user", "content": request}
    ]

    response = requests.post(GPT["url"], json=GPT["params"], headers=GPT["headers"])

    return response.json()["result"]


# # Функция для отправки запроса на Gemini
# def send_to_gemini(prompt):
#     headers = {
#         "Authorization": f"Bearer {GEMINI_API_TOKEN}",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "message": prompt
#     }

#     response = requests.post(GEMINI_URL, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Failed to contact Gemini API: {response.status_code}"}