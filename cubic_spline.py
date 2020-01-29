#! /usr/bin/env python3

'''
Cubic spline plot

This script has several functions:

- Estimate a cubic spline for one X and one Y
- Plot the raw data as a scatter plot
- Plot the cubic spline as a line plot

Specific to Linux:
time -f '%e' ./cubic_spline.py
./cubic_spline.py
'''


import numpy as np
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import CubicSpline as cs


c = cm.Paired.colors


def main():
    x_axis_label, y_axis_label, axis_title = (
        'Independent value',
        'Dependent value',
        'Cubic Spline'
    )
    raw_data = read_data_file()
    raw_data_x_values = raw_data.iloc[:, 0]
    raw_data_y_values = raw_data.iloc[:, 1]
    x2 = np.arange(-0.5, 9.6, 0.1)  # create x from 0.5 to 9.5, increment 0.1
    y2 = cs(raw_data_x_values, raw_data_y_values)
    ax = plot_scatter_line(raw_data_x_values, raw_data_y_values,
                      x2, y2,
                      x_axis_label, y_axis_label, axis_title)
    despine(ax)
    ax.figure.savefig('cubic_spline.svg', format='svg')


def read_data_file():
    '''
    The data file is presumed to have an index (row names or values),
    a first column with x values, and a second column with y values.
    '''
    while True:
        file_name = input('CSV file name to read? ')
        try:
            data = pd.read_csv(file_name, index_col=None)
        except FileNotFoundError:
            print(f'File {file_name} does not exist. Please try again.')
        else:
            return data


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_scatter_line(raw_data_x_values, raw_data_y_values,
                 x2, y2,
                 x_axis_label, y_axis_label, axis_title):
    figure_width_height = (8, 6)
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(raw_data_x_values, raw_data_y_values, marker='o', linestyle='None',
            color=c[1], label='data')
    ax.plot(x2, y2(x2), marker='None', linestyle='-',
            color=c[5], label='cubic spline')
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.legend(frameon=False)
    return ax


if __name__ == '__main__':
    main()
