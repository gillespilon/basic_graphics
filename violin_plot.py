#! /usr/bin/env python3

'''
Violin plot using matplotlib.

time -f '%e' ./vioilin_plot.py
./vioilin_plot.py
'''

import matplotlib.pyplot as plt
import matplotlib.axes as axes
import pandas as pd
import numpy as np


figure_size = (12, 8)
np.random.seed(10)
nparray1 = np.random.normal(100, 10, 200)
nparray2 = np.random.normal(80, 30, 200)
nparray3 = np.random.normal(90, 20, 200)
nparray4 = np.random.normal(70, 25, 200)
# use np.ndarray
data = [nparray1, nparray2, nparray3, nparray4]
print(type(nparray1))
print(type(data))
fig = plt.figure(figsize=figure_size)
ax = fig.add_subplot(111)
ax.violinplot(
        data,
        showmedians=True
        )
fig.savefig(
    fname='violinplot_from_ndarrays.svg'
)
# use pd.DataFrame
data2 = pd.DataFrame(data=[nparray1, nparray2, nparray3, nparray4]).T
data2.columns = ['a', 'b', 'c', 'd']
fig = plt.figure(figsize=figure_size)
ax = fig.add_subplot(111)
ax.violinplot(
        [data2['a'], data2['b'], data2['c'], data2['d']],
        showmedians=True
        )
fig.savefig(
    fname='violinplot_from_dataframe.svg'
)
