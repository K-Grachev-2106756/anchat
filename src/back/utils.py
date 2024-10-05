from config import BASE_PROMPT, hf_request_params, hf_client


# Функция для отправки запроса на Hugging Face
def send_to_hugging_face(request):
    result = []

    hf_request_params["messages"] = [
        {"role": "system", "content": BASE_PROMPT}, {"role": "user", "content": request}
    ]

    for message in hf_client.chat_completion(**hf_request_params):
        result.append(message.choices[0].delta.content)
    
    return "".join(result)


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