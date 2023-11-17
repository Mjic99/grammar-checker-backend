from happytransformer import HappyTextToText, TTSettings
from flask import Flask, request

app = Flask(__name__)

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)

@app.route("/api/correct", methods=['POST'])
def correct():
    user_text = request.json['text']
    result = happy_tt.generate_text(f"grammar: {user_text}", args=args)
    text = result.text.strip('.')

    return {
        'text': text
    }
