import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



# Sample data to predict (for example: area, number of rooms, and location)
def predictdiabetes(data1,data2) :
    model1=joblib.load("models/diabetes.joblib")

    data_to_predict = np.array([[data1,data2]]) 
    prediction = model1.predict(data_to_predict)
    prediction1=prediction[0]
    print(prediction[0])
    return prediction[0]
    
def predictblood(data1,data2):
    model = joblib.load('models/blood1.joblib')
    data_to_predict = np.array([[data1,data2]]) 
    prediction = model.predict(data_to_predict)
    print(prediction[0])
    return prediction[0]

def checkdiabetesgoodorbad(data1, data2):
    model1 = joblib.load("models/diabetes.joblib")
    data_to_predict = np.array([[data1, data2]])
    prediction = model1.predict(data_to_predict)
    prediction1 = prediction[0]
    
    # Load the data and filter by cluster
    data = pd.read_csv("data1/group/diabetes.csv")
    filtered_data = data[data["cluster"] == prediction1]
    print(filtered_data)
    
    # Calculate the mean and standard deviation of the diabetes values in the filtered cluster
    diabetes_mean = filtered_data["Diabetes"].mean()
    
    std_dev = filtered_data["Diabetes"].std()
    
    
    # Calculate deviation from mean
    deviation = data2 - diabetes_mean
    deviation_in_sd = deviation / std_dev 
    print(deviation_in_sd)
    
    # Categorize the diabetes value
    if deviation_in_sd <= 1:
        return ("The Diabetes level is normal.")
    elif deviation_in_sd <= 2:
        return ("The Diabetes level is slightly high; you may need a diet.")
    else:
        return ("The Diabetes level is too high; you should follow a strict diet.")
        

# Example usage
def bloodpressuregoodorbad(data1, data2):
    model1 = joblib.load("models/blood1.joblib")
    data_to_predict = np.array([[data1, data2]])
    prediction = model1.predict(data_to_predict)
    prediction1 = prediction[0]
    
    # Load the data and filter by cluster
    data = pd.read_csv("data1/group/blood_pressure.csv")
    filtered_data = data[data["cluster"] == prediction1]
    print(filtered_data)
    
    # Calculate the mean and standard deviation of the diabetes values in the filtered cluster
    diabetes_mean = filtered_data["BloodPressure"].mean()
    
    std_dev = filtered_data["BloodPressure"].std()
    
    
    # Calculate deviation from mean
    deviation = data2 - diabetes_mean
    deviation_in_sd = deviation / std_dev 
    print(deviation_in_sd)
    
    # Categorize the diabetes value
    if deviation_in_sd <= 1:
        return ("The bp level is normal.")
    elif deviation_in_sd <= 2:
        return ("The bp level is slightly high; you may need a diet.")
    else:
        return ("The bp level is too high; you should follow a strict diet.")




def dietdiabetes(value):
    data=pd.read_csv("diet data/age_diabetes.csv",encoding="latin1")
    print(data.head())
    value_to_check = value

# Use lambda with apply to check if the value is within the range
    data['In_Range'] = data['Value Range'].apply(lambda x: int(x.split('-')[0]) <= value_to_check <= int(x.split('-')[1]))
    data=data[data["In_Range"]==True]

# Print the DataFrame with the results
    return (data[['Morning Meal', 'Midday Meal',
       'Night Meal', 'Calories', 'Protein (g)', 'Carbohydrates (g)',
       'Fats (g)', 'Fiber (g)']])


def dietbp(value):
    data=pd.read_csv("diet data/bloodpressure(diet).csv",encoding="latin1")
    print(data.head())
    value_to_check = value

# Use lambda with apply to check if the value is within the range
    data['In_Range'] = data['Value Range'].apply(lambda x: int(x.split('-')[0]) <= value_to_check <= int(x.split('-')[1]))
    data=data[data["In_Range"]==True]

# Print the DataFrame with the results
    return (data[['Morning Meal', 'Midday Meal',
       'Night Meal', 'Calories', 'Protein (g)', 'Carbohydrates (g)',
       'Fats (g)', 'Fiber (g)']])


    



     

  



 

 
 
 

    
   

 






