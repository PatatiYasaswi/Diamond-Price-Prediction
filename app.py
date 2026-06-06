import streamlit as st
import pickle
import numpy as np
import time

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="Diamond Price Prediction",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open('diamond_price_model.pkl', 'rb'))

# ---------------- TITLE ---------------- #

st.markdown("""
<h1 style='text-align:center; color:#4B0082;'>
Diamond Price Prediction System
</h1>
""", unsafe_allow_html=True)

st.write("Predict the estimated market price of a diamond.")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Diamond Features")

st.sidebar.info(
    "Enter all diamond details carefully for better prediction accuracy."
)

# Inputs

carat = st.sidebar.number_input(
    "Carat",
    min_value=0.0,
    step=0.1
)

cut = st.sidebar.selectbox(
    "Cut",
    ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
)

color = st.sidebar.selectbox(
    "Color",
    ['D', 'E', 'F', 'G', 'H', 'I', 'J']
)

clarity = st.sidebar.selectbox(
    "Clarity",
    ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
)

depth = st.sidebar.number_input("Depth")

table = st.sidebar.number_input("Table")

x = st.sidebar.number_input("X Dimension")

y = st.sidebar.number_input("Y Dimension")

z = st.sidebar.number_input("Z Dimension")

# ---------------- HOME MESSAGE ---------------- #

st.info(
    "Add the diamond details in the left sidebar and click Predict Price."
)

# ---------------- ENCODING ---------------- #

cut_dict = {
    'Fair': 0,
    'Good': 1,
    'Very Good': 2,
    'Premium': 3,
    'Ideal': 4
}

color_dict = {
    'D': 0,
    'E': 1,
    'F': 2,
    'G': 3,
    'H': 4,
    'I': 5,
    'J': 6
}

clarity_dict = {
    'I1': 0,
    'SI2': 1,
    'SI1': 2,
    'VS2': 3,
    'VS1': 4,
    'VVS2': 5,
    'VVS1': 6,
    'IF': 7
}

# Convert Inputs

cut = cut_dict[cut]
color = color_dict[color]
clarity = clarity_dict[clarity]

# Currency Conversion

usd_to_inr = 83

# ---------------- PREDICTION BUTTON ---------------- #

if st.button("Predict Price"):

    # Loading Animation

    with st.spinner("Analyzing diamond features..."):
        time.sleep(2)

    # Features Array

    features = np.array([[
        carat,
        cut,
        color,
        clarity,
        depth,
        table,
        x,
        y,
        z
    ]])

    # Prediction

    prediction = model.predict(features)[0]

    # INR Conversion

    inr_price = prediction * usd_to_inr

    # ---------------- RESULT NUMBERS ---------------- #

    st.subheader("Predicted Price")
    st.write(f"USD: {prediction:,.2f}")
    st.write(f"INR: {inr_price:,.0f}")

# ---------------- INSTRUCTIONS ---------------- #

st.markdown("---")

st.subheader("Instructions")

st.write("""
1. Enter all diamond details from the left sidebar.

2. Click on Predict Price.

3. The system will estimate:
   - Diamond price in USD
   - Diamond price in INR
""")