import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load('water_model.pkl')

st.title("Water Potability Prediction")
st.write("Enter water quality values to check if water is drinkable or not")

# Inputs - same order as training
ph = st.slider("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 400.0, 200.0)
solids = st.number_input("Solids", 0.0, 60000.0, 20000.0)
chloramines = st.number_input("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0, 300.0)
conductivity = st.number_input("Conductivity", 0.0, 800.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 15.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 150.0, 70.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

if st.button("Predict"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate,
                          conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Water is POTABLE - Safe to Drink")
    else:
        st.error("❌ Water is NOT POTABLE - Not Safe to Drink")