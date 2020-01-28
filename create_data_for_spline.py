#! /usr/bin/env python3

'''
Create a dataframe with two columns for cubic_spline.py
'''


import pandas as pd
import numpy as np


filename = ('data_file.csv')
columns = ['data_x_values', 'data_y_values']
data_x_values = np.arange(10)
data_y_values = np.sin(data_x_values)
array = np.array([data_x_values, data_y_values])
data = pd.DataFrame(
    array.T,
    columns=columns
)
data.to_csv(filename)
