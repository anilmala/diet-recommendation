# Personalized Diet Recommendation System for Diabetes and High Blood Pressure

This project provides a personalized diet recommendation system for individuals with diabetes and high blood pressure. It uses machine learning to group patients based on similar health characteristics, predict the user's group, and calculate their deviation from the group average. Based on the user's blood pressure, diabetes levels, and age, it suggests a tailored diet plan to support better health management.

## Features
- **Clustering of Patients**: Groups individuals based on age, blood pressure, and diabetes levels using K-means clustering.
- **Deviation Calculation**: Calculates the deviation of the user's input from the group's average.
- **Tailored Diet Recommendations**: Suggests morning, midday, and night meal plans based on the health characteristics.
- **Nutrition Information**: Displays the nutrition level and detailed meal breakdown.
  
## Technologies Used
- **Python**  
- **Streamlit** (for building the interactive app)  
- **Pandas** (for data manipulation)  
- **NumPy** (for numerical operations)  
- **Scikit-learn** (for clustering and model building)  
- **Matplotlib/Seaborn** (for visualization)  
- **Pickle** (for model serialization)

## Installation

To run the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/anilmala/diet-recommendation.git

