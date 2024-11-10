import pandas as pd
import numpy as np
import yaml
import os
from sklearn.preprocessing import StandardScaler


params=yaml.safe_load(open('params.yaml'))["preprocess"]
sc=StandardScaler()

def preprocess(input,input1,output,output1):
    data=pd.read_csv(input,index_col=None)
    data1=pd.read_csv(input1,index_col=None)
    data=sc.fit_transform(data)
    data1=sc.fit_transform(data1)
    data=pd.DataFrame(data,columns=["age","blood_pressure"])
    data1=pd.DataFrame(data1,columns=["age","diabetes"])
    os.makedirs(os.path.dirname(output),exist_ok=True)
    data.to_csv(output)
    os.makedirs(os.path.dirname(output1),exist_ok=True)
    data1.to_csv(output1)
if __name__=="__main__":
    preprocess(params["input"],params["input1"],params["output"],params["output1"])        
