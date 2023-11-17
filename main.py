from happytransformer import HappyTextToText, TTSettings
from flask import Flask, request

app = Flask(__name__)

model = HappyTextToText("T5", model_name="train/model/")
args = TTSettings(num_beams=5, min_length=1)

@app.route("/api/correct", methods=['POST'])
def correct():
    user_text = request.json['text']
    result = model.generate_text(f"grammar: {user_text}", args=args)
    text = result.text.strip('.')

    return {
        'text': text
    }
