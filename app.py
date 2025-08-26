import streamlit as st
import pandas as pd
import joblib

model = joblib.load("housing_price_model.pkl")

st.title("🏡 House Price Prediction App")
st.write("Fill in the house details below to predict its price")

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
sqft_living = st.number_input("Living Area (sqft)", min_value=500, max_value=10000, value=2000)
sqft_lot = st.number_input("Lot Size (sqft)", min_value=500, max_value=50000, value=5000)
floors = st.number_input("Floors", min_value=1, max_value=5, value=1)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000)
zipcode = st.number_input("Zipcode", min_value=98000, max_value=99999, value=98100)

input_data = pd.DataFrame([[
    bedrooms,
    bathrooms,
    sqft_living,
    sqft_lot,
    floors,
    yr_built,
    zipcode
]], columns=["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "year_built", "zipcode"])

if st.button("🔮 Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: **${prediction:,.2f}**")

