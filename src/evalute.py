from sklearn.cluster import KMeans
import pandas as pd
import pickle
from yaml import safe_load
import os
import joblib
# Load parameters from params.yaml
params = safe_load(open("params.yaml"))["train"]
params1 = safe_load(open("params.yaml"))["train2"]

def train_kmeans(data_path, n_clusters, model_path):
    
    data = pd.read_csv("data/preprocessed/age_blood_presure1.csv")

    # Train KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    joblib.dump(kmeans, "models/blood_pressure_model")

    
    
    
    # Predict clusters for the data and add to the DataFrame
    data["cluster"] = kmeans.predict(data)
    return data


if __name__ == "__main__":
    # Train the model and save it
    data = train_kmeans(params["data1"], n_clusters=3, model_path=params["model2"])
    print(data.head())  # Show a preview of the data with clusters
    
    # Predict clusters using the saved model
  