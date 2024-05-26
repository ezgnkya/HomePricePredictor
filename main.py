from flask import Flask, render_template, request, jsonify
from model_predict import predict_process
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")

if os.path.exists('log.csv'):
    df = pd.read_csv('log.csv', encoding='utf-8-sig')
else:
    columns = ['Bina Yaşı', 'Oda Sayısı', 'Brüt Metrekare Alanı', 'Mahalle', 'Tahmin Edilen Fiyat']
    df = pd.DataFrame(columns=columns)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/sss.html')
def sss():
    return render_template('sss.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    price = predict_process(build_age=data['age'],
                            gross_square=int(data['gross_square']),
                            room_count=data['room'],
                            town_name=data['neighborhood'])
    price = "{:,.0f}".format(price).replace(',', '.')

    global df
    new_row = {'Bina Yaşı': data['age'],
               'Oda Sayısı': data['room'],
               'Brüt Metrekare Alanı': data['gross_square'],
               'Mahalle': data['neighborhood'],
               'Tahmin Edilen Fiyat': price}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv('log.csv', index=False, encoding='utf-8-sig')

    return jsonify({'predicted_price': f"{price} TL"})


if __name__ == "__main__":
    app.run(debug=True)
