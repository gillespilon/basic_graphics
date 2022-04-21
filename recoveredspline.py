#! /usr/bin/env python3
"""
Cubic spline plot

time -f '%e' ./cubic_spline.py
./cubic_spline.py
"""

from scipy.interpolate import CubicSpline as cs
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np

colour1 = '#0077bb'
colour2 = '#33bbee'


def main():
    x_axis_label, y_axis_label, axis_title = (
        'Independent value', 'Dependent value', 'Cubic Spline'
    )
    x1 = np.arange(10)  # create x values from 0 to 9, increments of 1
    y1 = np.sin(x1)
    x2 = np.arange(-0.5, 9.6, 0.1)  # create x from 0.5 to 9.5, increment 0.1
    y2 = cs(x1, y1)
    print(type(x1))
    print(type(y1))
    print(type(x2))
    print(type(y2))
    ax = cubic_spline(x1, y1, x2, y2, x_axis_label, y_axis_label, axis_title)
    ds.despine(ax=ax)
    ax.figure.savefig(
        fname='cubic_spline.svg',
        format='svg'
    )


def cubic_spline(x1, y1, x2, y2, x_axis_label, y_axis_label, axis_title):
    figure_width_height = (8, 6)
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(x1, y1, marker='o', linestyle='None',
            color=colour1, label='data')
    ax.plot(x2, y2(x2), marker='None', linestyle='-',
            color=colour2, label='cubic spline')
    ax.set_title(
        label=axis_title,
        
    )
    ax.set_xlabel(
        xlabel=x_axis_label,
        
    )
    ax.set_ylabel(
        ylabel=y_axis_label,
        
    )
    ax.legend(frameon=False)
    return ax


if __name__ == '__main__':
    main()
