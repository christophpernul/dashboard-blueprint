"""
This file is used to provide all functionality for data preprocessing.
"""
import pandas as pd
from scipy.special import y1

def load_date():
    start = 10
    end = 2000
    data = pd.DataFrame({
        "x": [x/100 for x in range(start, end)],
        "y": [2*x/100 + 42 for x in range(start, end)],
        "z": [y1(x/100) for x in range(start, end)]
    })
    return(data)

def preprocess_data(data):
    return(data)

def get_average(data):
    return(data["y"].mean())