from flask import Flask, request, jsonify
from utils.model import load_model, predict_image
from utils.sequence import predict_sequence
import os

app = Flask(__name__)
model = load_model()

@app.route('/')
def home():
    return "Flip Classifier API is running..."

@app.route('/predict-single', methods=['POST'])
def predict_single():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    img_file = request.files['image']
    result = predict_image(model, img_file)
    return jsonify(result)

@app.route('/predict-sequence', methods=['POST'])
def predict_seq():
    files = request.files.getlist('images')
    if not files or len(files) == 0:
        return jsonify({"error": "No images uploaded"}), 400
    result = predict_sequence(model, files)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
