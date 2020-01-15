#! /usr/bin/env python3

'''
Line plot, performance to target

time -f '%e' ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
'''

import pandas as pd
import matplotlib
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.ticker import NullFormatter, NullLocator


matplotlib.use('Cairo')
c = cm.Paired.colors
pd.plotting.register_matplotlib_converters(explicit=True)


def despine(ax: axes.Axes) -> None:
    'Remove the top and right spines of a graph'
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_two_lines(data, axis_title, x_axis_label, y_axis_label):
    figure_width_height = (8, 6)
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(data['Date'], data['Target'], label='Target',
            linestyle='-', color=c[0])
    ax.plot(data['Date'], data['Actual'], label='Actual', marker='o',
            linestyle='-', color=c[1])
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%y-%m'))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.legend(frameon=False)
    return ax


if __name__ == '__main__':
    data = pd.read_csv('actual_vs_target.csv', parse_dates=['Date'])
    axis_title, x_axis_label, y_axis_label = ('Date', 'USD',
                                              'Savings Target vs Actual')
    ax = plot_two_lines(data, axis_title, x_axis_label, y_axis_label)
    despine(ax)
