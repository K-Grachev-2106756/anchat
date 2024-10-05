import os

from dotenv import load_dotenv
load_dotenv()

from huggingface_hub import InferenceClient


BASE_PROMPT = """
    You are Yui Hirasawa - the main character of the Japanese comedy manga "K-On!" ("light music"). 
    She became the guitarist and lead singer of the school band "Ho-Kago Tea Time". She is very kind, 
    open and friendly, loves to hug and shake hands, loves everything cute, colorful and fabulous, 
    loves fun, but at the same time she is lazy and disorganized.
    """

MAX_TOKEN = 500

HF = {
    "client": InferenceClient(api_key=os.getenv("HUGGING_FACE_API_TOKEN")),
    "params": {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "max_tokens": MAX_TOKEN,
        "stream": True,
    }
}

GPT = {
    "url": "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2",
    "params": {
        "system_prompt": BASE_PROMPT,
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": MAX_TOKEN,
        "web_access": False,
    },
    "headers": {
        "x-rapidapi-key": os.getenv("RAPID_API_TOKEN"),
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json",
    },
}


#GEMINI_URL = "https://api.gemini.com/v1/chat"