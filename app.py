import streamlit as st
import joblib
import numpy as np
from datetime import datetime

# Load the model
model_path = 'weather_model.pkl'  # Ensure this path is correct
model = joblib.load(model_path)

# Title of the app
st.title("Weather Prediction App")

# User input for the date
date_input = st.date_input("Select Date", value=datetime.today())  # Default is today’s date

# Temperature input
temp_input = st.number_input("Temperature (°C)", value=0.0, min_value=-100.0, max_value=100.0, step=0.1)

# Precipitation input (float)
precip_input = st.number_input("Precipitation (mm)", value=0.0, min_value=0.0, max_value=100.0, step=0.1)

# Wind input
wind_input = st.number_input("Wind Speed (km/h)", value=0.0, min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Weather"):
    # Convert the input values to appropriate types
    precipitation = float(precip_input)
    temp_min = float(temp_input)
    wind = float(wind_input)

    # Determine the season based on the selected date
    month = date_input.month
    if month in [11, 12, 1, 2]:
        season_encoded = 0  # Winter
    elif month in [3, 4, 5]:
        season_encoded = 1  # Summer
    elif month in [6, 7, 8, 9]:
        season_encoded = 2  # Rainy (Monsoon)
    else:
        season_encoded = 3  # Transition period to winter

    # Encode temperature
    if temp_min <= 18.0:
        temp_encoded = 0  # Very cold
    elif 18.0 < temp_min <= 24.0:
        temp_encoded = 1  # Cold
    elif 24.0 < temp_min <= 30.0:
        temp_encoded = 2  # Cool
    else:
        temp_encoded = 3  # Warm

    # Encode precipitation
    if precipitation == 0.0:
        precip_encoded = 0  # No Rain
    elif 0 < precipitation <= 10.0:
        precip_encoded = 1  # Light Rain
    elif 10 < precipitation <= 30.0:
        precip_encoded = 2  # Moderate Rain
    else:
        precip_encoded = 3  # Heavy Rain

    # Encode wind
    if wind < 12.0:
        wind_encoded = 0  # Light wind
    elif 12.0 <= wind < 24.0:
        wind_encoded = 1  # Moderate wind
    elif 24.0 <= wind < 30.0:
        wind_encoded = 2  # Strong wind
    else:
        wind_encoded = 3  # Very strong wind

    # Create feature array for prediction
    input_features = np.array([[season_encoded, temp_encoded, precip_encoded, wind_encoded]])

    # Sample possible weather states (representing different weather conditions)
    sample_weather = np.linspace(0, 2, 3)  # We have 3 weather conditions: fog (0), rain (1), sun (2)

    # Find the most probable weather condition based on the model
    likelihood_scores = []
    for weather in sample_weather:
        # Create the full feature vector (including the weather condition)
        current_day = np.array([season_encoded, temp_encoded, precip_encoded, wind_encoded, weather])
        
        # Evaluate the likelihood score (you might need to adjust model scoring based on your model)
        likelihood_scores.append(model.score(current_day.reshape(1, -1)))  # Reshape to (1, 5) for scoring

    # Determine the most probable weather condition
    most_probable_weather = sample_weather[np.argmax(likelihood_scores)]

    # Decode the weather condition
    weather_conditions = {0: 'fog', 1: 'rain', 2: 'sun'}
    predicted_weather_condition = weather_conditions.get(most_probable_weather, 'Unknown')

    # Display the predicted weather condition
    st.success(f"Predicted Weather Condition: {predicted_weather_condition}")
