import joblib
# Load the model from the specified location
loaded_model = joblib.load("models/blood1.joblib")

# Use the loaded model for predictions
print(loaded_model.predict([[2, 2]]))  # Example prediction
