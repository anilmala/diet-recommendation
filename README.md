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

Follow the instructions below to set up and run the project locally:

### 1. Clone the repository:
```bash
git clone https://github.com/anilmala/diet-recommendation.git
cd diet-recommendation

### 2. Install the required dependencies:
To install the required dependencies, create a virtual environment (recommended) and install all the packages listed in the requirements.txt file:
```bash
pip install -r requirements.txt

### 3. Run the Streamlit app:
Once the dependencies are installed, you can run the Streamlit app locally:
```bash
streamlit run app.py

## Contribution
Feel free to fork this repository and submit pull requests. For any issues or suggestions, open a GitHub issue, and we’ll address it promptly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Scikit-learn for clustering techniques.
Streamlit for creating the interactive app.
