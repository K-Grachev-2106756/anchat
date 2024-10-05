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

hf_client = InferenceClient(api_key=os.getenv("HUGGING_FACE_API_TOKEN"))
hf_request_params = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "max_tokens": 500,
    "stream": True,
}

#GEMINI_URL = "https://api.gemini.com/v1/chat"