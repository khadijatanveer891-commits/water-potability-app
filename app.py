import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Water Potability", page_icon="💧", layout="centered")

# --- DARK GLASS + HOVER - SAFE CSS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617 0%, #0A1628 50%, #0E2A47 100%) !important;
}
h1 { color: white !important; text-align: center; }
p, label, span { color: #E0F2FE !important; }
h3 { color: #7DD3FC !important; }

/* Glass effect on every container - NO DIV NEEDED */
div[data-testid="stVerticalBlock"] > div {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 15px;
    transition: all 0.3s ease;
}
div[data-testid="stVerticalBlock"] > div:hover {
    border: 1px solid rgba(0,180,216,0.6);
    box-shadow: 0 10px 30px rgba(0,180,216,0.2);
    transform: translateY(-2px);
}

/* Button Glow + Hover */
.stButton>button {
    background: linear-gradient(90deg, #00B4D8, #2563EB) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 12px 30px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    width: 100%;
    box-shadow: 0 0 20px rgba(0,180,216,0.5);
    transition: all 0.3s ease !important;
}
.stButton>button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 0 35px rgba(0,180,216,0.9) !important;
}
</style>
""", unsafe_allow_html=True)

st.title("💧 Water Potability Prediction")
st.markdown("<p style='text-align:center;'>Check if your water is safe to drink</p>", unsafe_allow_html=True)

model = joblib.load('water_model.pkl')

col1, col2 = st.columns(2)
with col1:
    ph = st.slider("pH", 0.0, 14.0, 7.0)
    hardness = st.slider("Hardness", 0.0, 400.0, 150.0)
    solids = st.slider("Solids", 0.0, 60000.0, 20000.0)
    chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
    sulfate = st.slider("Sulfate", 0.0, 500.0, 250.0)
with col2:
    conductivity = st.slider("Conductivity", 0.0, 1000.0, 400.0)
    organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 10.0)
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 150.0, 70.0)
    turbidity = st.slider("Turbidity", 0.0, 10.0, 4.0)

if st.button("Predict Potability →"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    pred = model.predict(features)
    if pred[0] == 1:
        st.success("✅ Water is POTABLE - Safe to Drink")
        st.balloons()
    else:
        st.error("❌ Water is NOT POTABLE - Not Safe to Drink")
