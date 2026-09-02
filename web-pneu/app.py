from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
import os

app = Flask(__name__)

# LOAD MODEL & ENCODER
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'model', 'calibrated.pkl')
encoder_path = os.path.join(BASE_DIR, 'model', 'label_encoders.pkl')

model = joblib.load(model_path)
label_encoders = joblib.load(encoder_path)

# HALAMAN UTAMA
@app.route('/')
def index():
    prediction = request.args.get('prediction')
    return render_template('index.html', prediction_text=prediction)

# PREDIKSI
@app.route('/predict', methods=['POST'])
def predict():

    try:
        # AMBIL INPUT DARI FORM
        input_data = request.form.to_dict()
        feature_order = [
            'agecat3', 'sex', 'tb', 'crd', 'diabetes', 'cvd',
            'lowBP', 'confusion', 'rr_cat', 'bun_cat',
            'temp102', 'oxy_sat_90', 'tlc_cat', 'anemia'
        ]
        processed = {}

        for col in feature_order:
            value = request.form.get(col)

            if col in label_encoders:
                # pakai encoder
                processed[col] = label_encoders[col].transform([value])[0]
            else:
            # langsung angka
                processed[col] = float(value)
            print(col, ":", processed[col])


        data = np.array([[processed[col] for col in feature_order]])
        print("\n===== DEBUG FLASK =====")

        # 1. raw input
        print("RAW INPUT:", input_data)

        # 2. hasil encoding per fitur
        for col in feature_order:
            print(col, ":", processed[col])

        # 3. data final
        print("DATA FLASK:", data)

        # 4. probabilitas
        print("PROBA FLASK:", model.predict_proba(data))

        print("========================\n")
        # PREDIKSI
        proba = model.predict_proba(data)[0]
        kelas = model.classes_

        # mapping probabilitas ke kelas asli
        prob_dict = dict(zip(kelas, proba))

        # ambil kelas dengan probabilitas terbesar
        prediction = kelas[np.argmax(proba)]

        prob_tidak_icu = prob_dict[0]
        prob_icu = prob_dict[1]

        # INTERPRETASI HASIL
        if prediction == 1:
            label = "Parah"
            prob = prob_icu
        else:
            label = "Ringan"
            prob = prob_tidak_icu

        result = f"{label} ({prob*100:.2f}%)"

        return redirect(url_for('index',prediction=result,) + '#result-section')

    except Exception as e:
        return f"Error: {str(e)}"
# R
if __name__ == '__main__':
    app.run(debug=True)