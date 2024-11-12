from yaml import safe_load
import yaml
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
import pickle
import joblib

params=yaml.safe_load(open('params.yaml'))["train3"]

def predictdata(data_path):
    data=pd.read_csv("data/preprocessed/age_blood_presure1.csv")
    model=joblib.load("models/blood1.joblib")
    os.makedirs(os.path.dirname(data_path),exist_ok=True)
    data["cluster"]=model.predict(data)
    data.to_csv(data_path)
if __name__=="__main__":
    predictdata(params["bloodpressure"]) 


def predictdata1(data_path):
    data=pd.read_csv("data/preprocessed/age_diabetess1.csv")
    model=joblib.load("models/diabetes.joblib")
    os.makedirs(os.path.dirname(data_path),exist_ok=True)
    data["cluster"]=model.predict(data)
    data.to_csv(data_path)
if __name__=="__main__":
    predictdata1(params["diabetes"])     







   







