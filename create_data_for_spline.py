#! /usr/bin/env python3

'''
Create a dataframe with two columns for cubic_spline.py

time -f '%e' ./create_data_for_spline.py
./create_data_for_spline.py
'''


import pandas as pd
import numpy as np


filename = ('cubic_spline_raw_data.csv')
columns = ['raw_data_x', 'raw_data_y']
raw_data_x_values = np.arange(10)
raw_data_y_values = np.sin(raw_data_x_values)
array = np.array([raw_data_x_values, raw_data_y_values])
data = pd.DataFrame(
    array.T,
    columns=columns
)
data.to_csv(filename, index=False)
