from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import os
import requests
import numpy as np  # Tambahkan ini untuk membantu konversi tipe data

from batik import predict

app = Flask(__name__)
CORS(app)

@app.route('/batik', methods=['POST'])
def batik():
    img_param = request.form['img']
    
    # Mendapatkan hasil prediksi
    predicted_class_name, confidence = predict(img_param)
    
    # Konversi float32 ke Python float standar agar bisa di-serialisasi JSON
    confidence_float = float(confidence)
    
    print("Typenya adalah ", type(img_param))
    try:
        data = {
            'code': 200,
            'message': 'Berhasil memprediksi!',
            'prediksi': {
                'class': predicted_class_name,
                'confidence': confidence_float  # Gunakan nilai yang sudah dikonversi
            }
        }
        
        return make_response(jsonify(data)), 200
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    

@app.route('/test', methods=['GET'])
def test():
    return 'Hallow ddd'

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)