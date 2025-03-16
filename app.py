from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("car_price_model.pkl")

@app.route('/')
def home():
    return "Car Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Convert data to DataFrame
    df = pd.DataFrame(data, index=[0])
    
    # OneHotEncoding (Ensure correct format)
    df = pd.get_dummies(df, drop_first=True)

    # Predict price
    prediction = model.predict(df)
    
    return jsonify({"predicted_price": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
