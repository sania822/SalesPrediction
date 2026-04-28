import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title(" Sales Prediction App")

st.write("Enter advertising spend values:")

# Inputs
tv = st.number_input("TV Spend", min_value=0.0)
radio = st.number_input("Radio Spend", min_value=0.0)
news = st.number_input("Newspaper Spend", min_value=0.0)

# Feature engineering (same as training)
total = tv + radio + news
tv_radio = tv * radio
tv_news = tv * news

if st.button("Predict Sales"):
    input_data = np.array([[tv, radio, news, total, tv_radio, tv_news]])
    prediction = model.predict(input_data)

    st.success(f" Predicted Sales: {prediction[0]:.2f}")