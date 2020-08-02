#! /usr/bin/env python3

'''
Line plots of actual and target data, and regression line of actual data.

- Line plot of target value (y) versus date (x)
- Line plot of actual value (y) versus date (x)
- Line plot of predicted value (y) versus date (x) using linear regression

time -f '%e' ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
'''

from typing import Tuple

import matplotlib.pyplot as plt
import matplotlib.axes as axes
import statsmodels.api as sm
import matplotlib.cm as cm
import datasense as ds
import pandas as pd
import numpy as np


c = cm.Paired.colors
figure_width_height = (8, 6)


def main():
    data = pd.read_excel(
        'actual_vs_target.ods',
        engine='odf',
        parse_dates=['Date']
    )
    x_axis_label, y_axis_label, axis_title = (
        'Date', 'USD',
        'Savings Target vs Actual'
    )
    data = regression(data)
    fig, ax = plot_three_lines(
        data,
        axis_title,
        x_axis_label,
        y_axis_label
    )
    ds.format_dates(fig, ax)
    despine(ax)
    ax.figure.savefig('actual_vs_target.svg', format='svg')


def despine(ax: axes.Axes) -> Tuple[plt.figure, axes.Axes]:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''

    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_three_lines(
    data: pd.DataFrame,
    axis_title: str,
    x_axis_label: str,
    y_axis_label: str
) -> axes.Axes:
    '''
    Create three line plots:
    - Target vs date
    - Actual vs date
    - Predicted vs date
    '''

    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(
        data['Date'],
        data['TargetBalance'],
        label='TargetBalance',
        linestyle='-',
        color=c[0]
    )
    ax.plot(
        data['Date'],
        data['ActualBalance'],
        label='ActualBalance',
        linestyle='-',
        color=c[1],
        marker='.'
    )
    ax.plot(
        data['Date'],
        data['Predicted'],
        label='Predicted',
        linestyle='-',
        color=c[2]
    )
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.legend(frameon=False)
#     for row, text in enumerate(data['Annotation']):
#         print(type(data['Annotation']))
#         ax.annotate(text, (data['Date'][row],
#                            data['ActualBalance'][row]),
#                     xytext=(20, 0),
#                     textcoords='offset points',
#                     arrowprops=dict(arrowstyle="->"))
#     for item in data['Annotation']:
#         if item != np.nan :
#             print(item)
#         else:
#             pass
#     ax.annotate(
#         'USG bonus',
#         xy=('2020-03-15', 23275.12),
#         xytext=(20, 0),
#         textcoords='offset points',
#         arrowprops=dict(arrowstyle="->")
#     )
    return (fig, ax)


def regression(
    data: pd.DataFrame,
    model: str = 'linear'
) -> pd.DataFrame:
    '''
    Estimate a regression line.

    Y is a float
    X is a datetime64ns
    Convert X to a float with first value set to 0 number of days between
    subsequent values
    '''

    data['DateDelta'] = (data['Date'] - data['Date']
                         .min())/np.timedelta64(1, 'D')
    if model == 'linear':
        model = sm.OLS(
            data['ActualBalance'],
            sm.add_constant(data['DateDelta']),
            missing='drop'
        ).fit()
        data['Predicted'] = model.fittedvalues
    else:
        # TODO: quadratic, cubic, etc.
        print('Feature not implemented.')
    return data


if __name__ == '__main__':
    main()
