#! /usr/bin/env python3

'''
Create a line plot of weight and a fixed target line

time -f '%e' ./weight_loss_tracker.py
./weight_loss_tracker.py
'''

# TODO:
# - Confidence interval
# - Prediction interval

from typing import Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.cm as cm
import pandas as pd


c = cm.Paired.colors
figure_width_height = (8, 6)
fig_title = 'Weight loss'
file_name_data = 'weight.ods'
file_name_graph = 'weight.svg'
column_x = 'Date'
column_target = 'Target'
column_actual = 'Actual'
title = 'Plot of Weight Loss'
xlabel = 'Date'
ylabel = 'Weight (kg)'


def main():
    data = read_data(file_name_data)
    plot_line(
        data, column_x, column_target, column_actual,
        file_name_graph, figure_width_height, title, xlabel, ylabel
    )


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def read_data(filename: str) -> pd.DataFrame:
    data = pd.read_excel(filename, engine='odf', parse_dates=['Date'])
    return data


def plot_line(
    dataframe: pd.DataFrame,
    columnx: str,
    columntarget: str,
    columnactual: str,
    filenamegraph: str,
    figurewidthheight: Tuple[int, int],
    title: str,
    xlabel: str,
    ylabel: str
) -> None:
    fig = plt.figure(figsize=figurewidthheight)
    ax = fig.add_subplot(111)
    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.plot(
        dataframe[columnx],
        dataframe[columntarget],
        color=c[0]
    )
    ax.plot(
        dataframe[columnx],
        dataframe[columnactual],
        color=c[1],
        marker='.',
        markersize=10,
        linestyle='-'
    )
    ax.set_title(fig_title, fontweight='bold')
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_ylabel(ylabel, fontweight='bold')
    despine(ax)
    ax.figure.savefig(filenamegraph, format='svg')


if __name__ == '__main__':
    main()
