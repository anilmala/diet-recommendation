import joblib
import numpy as np



# Sample data to predict (for example: area, number of rooms, and location)
def predictdiabetes(data1,data2) :
    model1=joblib.load("models/diabetes.joblib")
    data_to_predict = np.array([[data1,data2]]) 
    prediction = model1.predict(data_to_predict)
    print(prediction)
    return prediction
    

 # 1200 sqft, 3 rooms, location 1 (could be encoded as a number)

# Use the model to predict
def predictblood(data1,data2):
    model = joblib.load('models/blood1.joblib')
    data_to_predict = np.array([[data1,data2]]) 
    prediction = model.predict(data_to_predict)
    print(prediction)
    return prediction 
predictblood(1,2)
    
   

 



