from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('./model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form
    lb = request.form['lb']
    lt = request.form['lt']
    kt = request.form['kt']
    km = request.form['km']
    grs = request.form['grs']

    # Buat array untuk prediksi
    input_data = np.array([[lb, lt, kt, km, grs]], dtype=float)

    # Prediksi
    prediction = model.predict(input_data)[0]
    prediction_milyar = prediction / 1000  # Konversi ke milyar

    return render_template('index.html', prediction_text=f'Prediksi harga rumah adalah: {prediction_milyar:.2f} milyar')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
