import requests

from config import HUGGING_FACE_URL, BASE_PROMPT, hf_headers


# Функция для отправки запроса на Hugging Face
def send_to_hugging_face(request):
    response = requests.post(HUGGING_FACE_URL, headers=hf_headers, json={"inputs": BASE_PROMPT.format(request)})
    
    if response.status_code == 200:
        return response.json()

    return {"error": f"Failed to contact Hugging Face API: {response.status_code}"}

# import json
# with open("1.json", "w", encoding="utf-8") as f:
#     json.dump(send_to_hugging_face("Hi. 2+2 = ?"), f, ensure_ascii=False, indent=4)

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