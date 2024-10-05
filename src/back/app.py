from flask import Flask, request, jsonify

from utils import send_to_hugging_face#, send_to_gemini


app = Flask(__name__)

# Эндпоинт для обработки запросов
@app.route("/process", methods=["POST"])
def process_request():
    try:
        # Получаем данные из запроса
        data = request.json
        prompt = data.get("prompt")

        print(prompt)

        if not prompt:
            return jsonify({"error": "Prompt is missing"}), 400

        # Формируем запрос для Hugging Face
        hugging_face_response = send_to_hugging_face(prompt)

        # # Формируем запрос для Gemini
        # gemini_response = send_to_gemini(prompt)

        # Возвращаем ответы от обеих моделей
        return jsonify({
            "hugging_face_response": hugging_face_response,
            # "gemini_response": gemini_response
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
