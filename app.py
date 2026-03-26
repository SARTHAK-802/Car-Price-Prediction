import streamlit as st
import pickle
import pandas as pd
import os

# Load model and columns safely
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'), 'rb'))
columns = pickle.load(open(os.path.join(BASE_DIR, 'columns.pkl'), 'rb'))

# Title
st.title("🚗 Car Price Prediction")

st.write("Fill details to predict car selling price")

# Inputs
year = st.number_input("Year of Purchase", 2000, 2025)
present_price = st.number_input("Present Price (Lakhs)")
kms_driven = st.number_input("Kilometers Driven")
owner = st.selectbox("Owner", [0, 1, 2, 3])

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Correct input dictionary (FIXED)
input_dict = {
    'car_age': 2025 - year,   # ✅ FIXED
    'Present_Price': present_price,
    'Kms_Driven': kms_driven, # ✅ FIXED
    'Owner': owner,
    'Fuel_Type_Diesel': 1 if fuel_type == "Diesel" else 0,
    'Seller_Type_Individual': 1 if seller_type == "Individual" else 0,
    'Transmission_Manual': 1 if transmission == "Manual" else 0
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Align columns
input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_df)
        st.success(f"💰 Estimated Price: ₹ {prediction[0]:.2f} Lakhs")
    except Exception as e:
        st.error(f"Error: {e}")