import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Set up the page
st.title("My First ML Dashboard")
st.write("This dashboard uses a saved machine learning model to make predictions!")

# Load the model (assuming you saved it as shown above)
@st.cache_resource
def load_model():
    with open('my_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Try to load the model
try:
    model = load_model()
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("Model file not found. Please train and save a model first.")
    # Create a dummy model for demonstration
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression()
    model.fit(X, y)

# Create input widgets
st.subheader("Make a Prediction")
input_value = st.number_input("Enter a value for prediction:", value=0.0)

# Make prediction when button is clicked
if st.button("Predict"):
    prediction = model.predict([[input_value]])
    st.write(f"Predicted value: {prediction[0]:.2f}")