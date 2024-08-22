import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open('car_price_prediction.model', 'rb') as model_file:
    model = pickle.load(model_file)


# Function to make predictions
def predict_price(year, transmission, engine, max_power):
    # Prepare the input data for prediction
    input_data = np.array([[year, transmission, engine, max_power]])
    # Make prediction
    prediction = model.predict(input_data)
    return np.exp(prediction[0])


# Streamlit app
st.title('Car Selling Price Prediction')

# Inputs
year = st.number_input('Year', min_value=1900, max_value=2024, value=2020)
transmission = st.selectbox('Transmission', ['Auto', 'Manual'])
engine = st.number_input('Engine (CC)', min_value=624, value=1462)
max_power = st.number_input('Max Power (HP)', min_value=68, value=90)

# Encode transmission
transmission_encoded = 1 if transmission == 'Auto' else 0

# Predict button
if st.button('Predict'):
    price = predict_price(year, transmission_encoded, engine, max_power)
    st.write(f'The predicted selling price is ${price:.2f}')
