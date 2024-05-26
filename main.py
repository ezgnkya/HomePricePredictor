from flask import Flask, render_template, request, jsonify
from model_predict import predict_process

app = Flask(__name__, template_folder="templates")


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
    return jsonify({'predicted_price': price})


if __name__ == "__main__":
    app.run(debug=True)
