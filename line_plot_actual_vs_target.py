#! /usr/bin/env python3

'''
Actual vs target line plots

- Line plot of target value (y) versus date (x)
- Line plot of actual value (y) versus date (x)
- Line plot of predicted value (y) versus date (x) using linear regression

time -f '%e' ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
'''


from typing import Tuple


import numpy as np
import pandas as pd
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import statsmodels.api as sm
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.ticker import NullFormatter, NullLocator


c = cm.Paired.colors
figure_width_height = (8, 6)


def main():
    data = pd.read_excel('actual_vs_target.ods',
                         engine='odf',
                         parse_dates=['Date'])
    x_axis_label, y_axis_label, axis_title = ('Date', 'USD',
                                              'Savings Target vs Actual')
    data = regression(data)
    ax = plot_three_lines(data, axis_title, x_axis_label, y_axis_label,
                          figure_width_height)
    despine(ax)
    ax.figure.savefig('actual_vs_target.svg', format='svg')
    ax.figure.savefig('actual_vs_target.png', format='png')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_three_lines(
    data: pd.DataFrame, axis_title: str, x_axis_label: str, y_axis_label: str,
    figure_width_height: Tuple[int, int]
):
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(data['Date'], data['TargetBalance'], label='TargetBalance',
            linestyle='-', color=c[0])
    ax.plot(data['Date'], data['ActualBalance'], label='ActualBalance',
            linestyle='-', color=c[1], marker='.')
    ax.plot(data['Date'], data['Predicted'], label='Predicted',
            linestyle='-', color=c[2])
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
#     for row, text in enumerate(data['Annotation']):
#         if len(text) > 0:
#             ax.annotate(text, (data['Date'][row],
#                                data['ActualBalance'][row]),
#                         xytext=(20, 0),
#                         textcoords='offset points',
#                         arrowprops=dict(arrowstyle="->"))
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%m'))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.legend(frameon=False)
    return ax


def regression(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Estimate a linear regression line
    Y is a float
    X is a datetime64ns
    Convert X to a float with first value set to 0 number of days between
    subsequent values
    '''
    data['DateDelta'] = (data['Date'] - data['Date']
                         .min())/np.timedelta64(1, 'D')
    model = sm.OLS(data['ActualBalance'], sm.add_constant(data['DateDelta']),
                   missing='drop').fit()
    data['Predicted'] = model.fittedvalues
    return data


if __name__ == '__main__':
    main()
