#! /usr/bin/env python3

'''
Weight loss tracker using a line plot and fixed target line

time -f '%e' ./weight_loss_tracker.py
./weight_loss_tracker.py
'''

# TODO:
# - Confidence interval
# - Prediction interval

import pandas as pd
import matplotlib
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import NullLocator


c = cm.Paired.colors
figure_width_height = (8, 6)
fig_title = 'Weight loss analysis'
file_name = 'weight.ods'
column_target = 'Target'
column_actual = 'Actual'
title = 'Plot of Weight Loss'
xlabel = 'Date'
ylabel = 'Weight (kg)'


matplotlib.use('Cairo')


def main():
    data = read_data(file_name)
    plot_line(data, column_target, column_actual, figure_width_height,
              title, xlabel, ylabel)


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def read_data(filename):
    data = pd.read_excel(filename, engine='odf', parse_dates=['Date'])
    return data


def plot_line(dataframe, columntarget, columnactual, figure_width_height,
              title, xlabel, ylabel):
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(
        dataframe[columntarget],
        color=c[0]
    )
    ax.plot(dataframe[
        columnactual],
        color=c[1],
        marker='.',
        markersize=10,
        linestyle='-'
    )
    ax.set_title('Scatter Plot of Weight Loss', fontweight='bold')
    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel('Weight (kg)', fontweight='bold')
    # ax.xaxis.set_minor_locator(NullLocator())
    # ax.xaxis.set_major_locator(DayLocator())
    # ax.xaxis.set_minor_formatter(NullFormatter())
    # ax.xaxis.set_major_formatter(DateFormatter('%d'))
    # ax.autoscale(enable=True)
    # despine(ax)
    ax.figure.savefig('weight.svg',
                      format='svg')


if __name__ == '__main__':
    main()
