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
from scipy.interpolate import CubicSpline as cs


c = cm.Paired.colors


def main():
    x_axis_label, y_axis_label, axis_title = (
        'Independent value', 'Dependent value', 'Cubic Spline'
    )
    x1 = np.arange(10)  # create x values from 0 to 9, increments of 1
    y1 = np.sin(x1)
    x2 = np.arange(-0.5, 9.6, 0.1)  # create x from 0.5 to 9.5, increment 0.1
    y2 = cs(x1, y1)
    ax = cubic_spline(x1, y1, x2, y2, x_axis_label, y_axis_label, axis_title)
    despine(ax)
    ax.figure.savefig('cubic_spline.svg', format='svg')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def cubic_spline(x1, y1, x2, y2, x_axis_label, y_axis_label, axis_title):
    figure_width_height = (8, 6)
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(x1, y1, marker='o', linestyle='None',
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
