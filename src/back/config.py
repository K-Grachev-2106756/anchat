import os

from dotenv import load_dotenv
load_dotenv()


HUGGING_FACE_MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"

HUGGING_FACE_URL = "https://api-inference.huggingface.co/models/{model_name}".format(model_name=HUGGING_FACE_MODEL_NAME)

BASE_PROMPT = "Imagine you are a cute anime girl and answer the following: '{}'. Your answer is:"

hf_headers = {
    "Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_TOKEN')}",
    "Content-Type": "application/json"
}

#GEMINI_URL = "https://api.gemini.com/v1/chat"