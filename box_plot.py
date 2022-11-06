#! /usr/bin/env python3

'''
Box plot using matplotlib.

time -f '%e' ./box_plot.py
./box_plot.py
'''

import matplotlib.pyplot as plt
import matplotlib.axes as axes
import pandas as pd
import numpy as np


nparray1 = np.random.normal(100, 10, 200)
nparray2 = np.random.normal(80, 30, 200)
nparray3 = np.random.normal(90, 20, 200)
nparray4 = np.random.normal(70, 25, 200)
np.random.seed(10)
figsize = (12, 8)
# use np.ndarray
data = [nparray1, nparray2, nparray3, nparray4]
print(type(nparray1))
print(type(data))
fig, ax = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=figsize
)
ax.boxplot(
        data,
        notch=True
        )
fig.savefig(fname='boxplot_from_ndarrays.svg')
# use pd.DataFrame
data2 = pd.DataFrame(data=[nparray1, nparray2, nparray3, nparray4])\
    .transpose()\
    .set_axis(
        labels=['a', 'b', 'c', 'd'],
        axis='columns'
    )
fig, ax = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=figsize
)
ax.boxplot(
        [data2['a'], data2['b'], data2['c'], data2['d']],
        notch=True
        )
fig.savefig(fname='boxplot_from_dataframe.svg')
