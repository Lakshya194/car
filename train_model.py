import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("car_data.csv")

# Selecting features and target variable
X = df[['kmdriven', 'fuel', 'sellertype', 'transmission', 'owner']]
y = df['sellingprice']  # Target variable

# Convert categorical variables to numerical using OneHotEncoding
X = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "car_price_model.pkl")

print("Model trained and saved successfully!")
