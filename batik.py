import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

import os
# from google.cloud import storage

# # Tetapkan variabel lingkungan ke path file kredensial
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./aa.json"


MODEL_PATH = "./model_acc93_valacc93.keras"


class_names  = ['Corak Insang',
 'Dayak',
 'Geblek Renteng',
 'Gentongan',
 'Kawung',
 'Kraton',
 'Megamendung',
 'Parang',
 'Pring Sedapur',
 'Simbut',
 'bali',
 'betawi',
 'celup',
 'cendrawasih',
 'ceplok',
 'ciamis',
 'garutan',
 'pekalongan',
 'priangan',
 'sekar',
 'sidoluhur',
 'sidomukti',
 'sogan',
 'tambal']


def load_model():
    """Load model dari file lokal"""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    
    print(f"Loading model from: {MODEL_PATH}")
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

# Load model saat import

model = load_model()
def predict(url):
    # Unduh gambar dari URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # Konversi gambar ke RGB jika memiliki channel alpha
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Resize gambar ke ukuran yang diharapkan model
    img = img.resize((150, 150))
    
    # Normalisasi nilai pixel
    img_array = np.array(img) / 255.0
    
    # Periksa bentuk array sebelum prediksi
    print(f"Image shape: {img_array.shape}")
    
    # Tambahkan dimensi batch
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prediksi
    predictions = model.predict(img_array)
    
    # Dapatkan kelas dengan probabilitas tertinggi
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_names[predicted_class]
    confidence = predictions[0][predicted_class]
    
    return predicted_class_name, confidence