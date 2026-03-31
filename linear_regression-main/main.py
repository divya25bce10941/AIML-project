import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math
from sklearn.metrics import confusion_matrix
import pickle as pkl
model = LinearRegression()

data = pd.read_csv("./data/insurance.csv")
def clean_data(data):
    data["sex"].replace(["male","female"],[0,1],inplace=True)
    encoder = LabelEncoder()
    label = encoder.fit_transform(data["smoker"])
    label2 = encoder.fit_transform(data["region"])
    data["smoker"] = label
    data["region"] = label2
    data = data.drop("region",axis=1)
    return data
data = clean_data(data)

x = data.drop("charges",axis=1)
y = data["charges"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


model.fit(x_train,y_train)
print(f"Accuracy : {model.score(x_test,y_test)*100}%")
with open("model.pkl","wb") as fileObj:
    pkl.dump(model,fileObj)
