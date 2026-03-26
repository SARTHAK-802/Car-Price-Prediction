import streamlit as st
import pickle
import pandas as pd
import os

# -------------------------------
# Load model and columns safely
# -------------------------------
BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "model.pkl")
columns_path = os.path.join(BASE_DIR, "columns.pkl")

model = pickle.load(open(model_path, "rb"))
columns = pickle.load(open(columns_path, "rb"))

# -------------------------------
# App Title
# -------------------------------
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("Car Price Prediction App")
st.markdown("### Predict the selling price of a used car")

# -------------------------------
# Input Section (Better UI)
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Purchase", min_value=2000, max_value=2025, value=2015)
    present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0)

with col2:
    owner = st.selectbox("Number of Owners", [0, 1, 2, 3])
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# -------------------------------
# Prepare Input Data (IMPORTANT)
# -------------------------------
input_dict = {
    'car_age': 2025 - year,
    'Present_Price': present_price,
    'Kms_Driven': kms_driven,
    'Owner': owner,
    'Fuel_Type_Diesel': 1 if fuel_type == "Diesel" else 0,
    'Seller_Type_Individual': 1 if seller_type == "Individual" else 0,
    'Transmission_Manual': 1 if transmission == "Manual" else 0
}

input_df = pd.DataFrame([input_dict])

# Align with training columns
input_df = input_df.reindex(columns=columns, fill_value=0)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_df)

        st.success(f"💰 Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")

    except Exception as e:
        st.error("⚠️ Something went wrong. Check model or inputs.")
        st.write(e)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Built with using Streamlit")