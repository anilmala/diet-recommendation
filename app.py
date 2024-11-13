import streamlit as st
import joblib
from src.utils import predictblood,predictdiabetes,checkdiabetesgoodorbad,bloodpressuregoodorbad,dietbp,dietdiabetes  # assuming your models are saved as .pkl files

# Load your models
diabetes_model = joblib.load("models/diabetes.joblib")  # replace with your model path
blood_pressure_model = joblib.load("models/blood1.joblib")  # replace with your model path
st.markdown(
    """
    <style>
    .main {
        background-image: url("https://www.w3schools.com/w3images/hospital.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .content-container {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }
    .title h1 {
        color: #1a73e8;
        font-weight: bold;
        text-align: center;
        padding-bottom: 10px;
    }
    .stNumberInput input {
        border: 1px solid #1a73e8;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton button:hover {
        background-color: #155a96;
        color: #e2e2e2;
    }
    /* Table styling */
    .styled-table {
        margin-top: 20px;
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }
    .styled-table th, .styled-table td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }
    .styled-table th {
        background-color: #1a73e8;
        color: white;
    }
    .styled-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .styled-table tr:hover {
        background-color: #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app layout
st.markdown('<div class="title"><h1>Personalized Diet App</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="content-container">', unsafe_allow_html=True)
# Streamlit app layout





# Streamlit app
st.title("Personalised Diet App")

# Input section
age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
diabetic_value = st.number_input("Enter Diabetic Value", min_value=0.0, max_value=500.0, step=0.1, format="%.1f")
blood_pressure = st.number_input("Enter Blood Pressure Value", min_value=0.0, max_value=300.0, step=0.1, format="%.1f")

# Prediction logic
if st.button("Predict"):
    if diabetic_value and not blood_pressure:
        prediction = predictdiabetes(age, diabetic_value)
        st.write(f"Diabetes Prediction: {prediction}")
        checking=checkdiabetesgoodorbad(age,diabetic_value)
        st.write({checking})
        table=dietdiabetes(diabetic_value)
        st.subheader("Diabtets diet")
        st.table(table)
        st.write("choose any one diet ")
        
    elif blood_pressure and not diabetic_value:
        prediction = predictblood(age, blood_pressure)
        st.write(f"Blood Pressure Prediction: {prediction}")
        checking=bloodpressuregoodorbad(age,blood_pressure)
        st.write(checking)
        table=dietbp(blood_pressure)
        st.subheader("Blood pressure diet ")
        st.table(table)
        st.write("chose any one diet ")
    else:
        st.warning("Please enter either a diabetic value or a blood pressure value, but not both.")
