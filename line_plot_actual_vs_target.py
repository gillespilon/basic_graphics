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
file_name_data = 'actual_vs_target.ods'
file_name_graph = 'actual_vs_target.svg'
x_axis_label, y_axis_label, axis_title = (
    'Date',
    'USD',
    'Savings Target vs Actual'
)
column_x, column_target, column_actual, column_predicted = (
    'Date',
    'TargetBalance',
    'ActualBalance',
    'Predicted'
)


def main():
    data = ds.read_file(
        filename=file_name_data,
        abscissa=column_x
    )
    data = regression(data)
    fig, ax = ds.plot_line_line_line_x_y1_y2_y3(
        X=data[column_x],
        y1=data[column_target],
        y2=data[column_actual],
        y3=data[column_predicted],
        figuresize=figure_width_height,
        labellegendy1=column_target,
        labellegendy2=column_actual,
        labellegendy3=column_predicted
    )
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.legend(frameon=False)
    ds.format_dates(fig, ax)
    despine(ax)
    ax.figure.savefig(file_name_graph, format='svg')


def despine(ax: axes.Axes) -> Tuple[plt.figure, axes.Axes]:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''

    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


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

    Parameters:
        data    : pd.DataFrame
        model   : str

    Returns:
        data    : pd.DataFrame
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
