#! /usr/bin/env python3
"""
Line plots of actual and target data, and regression line of actual data.

- Line plot of target value (y) versus date (x)
- Line plot of actual value (y) versus date (x)
- Line plot of predicted value (y) versus date (x) using linear regression

time -f '%e' ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
"""

from pathlib import Path
from typing import Tuple
from os import chdir

import matplotlib.pyplot as plt
import matplotlib.axes as axes
import statsmodels.api as sm
import datasense as ds
import pandas as pd
import numpy as np

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
chdir(Path(__file__).parent.__str__())  # required for cron


def main():
    data = ds.read_file(
        file_name=file_name_data,
        abscissa=column_x
    )
    data = regression(
        data=data,
        model='linear',
        columnx=column_x,
        columnactual=column_actual,
        columnpredicted=column_predicted
    )
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
    fig.savefig(file_name_graph, format='svg')


def despine(ax: axes.Axes) -> Tuple[plt.figure, axes.Axes]:
    """
    Remove the top and right spines of a graph.

    Parameters
    ----------
    ax : axes.Axes

    Example
    -------
    >>> despine(ax)
    """

    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def regression(
    data: pd.DataFrame,
    model: str,
    columnx: str,
    columnactual: str,
    columnpredicted: str
) -> pd.DataFrame:
    """
    Estimate a regression line.

    Parameters
    ----------
    data : pd.DataFrame
    model : str
    columnx : str
    columnactual : str
    columnpredicted : str

    Returns
    data : pd.DataFrame

    Example
    # TODO
    create an example for regression
    x generate 42 integers 1 to 42, increments of 1
    y generate y = mx + b
    where b = 69, m = 13
    ysubi = b +/- loc 69 scale 7 + m +/- loc 13 scale 4 * x
    """
    data['DateDelta'] = (data[columnx] - data[columnx].min())\
        / np.timedelta64(1, 'D')
    if model == 'linear':
        model = sm.OLS(
            endog=data[columnactual],
            exog=sm.add_constant(data['DateDelta']),
            missing='drop'
        ).fit()
        data[columnpredicted] = model.fittedvalues
    else:
        # TODO: quadratic, cubic, etc.
        print('Feature not implemented.')
    return data


if __name__ == '__main__':
    main()
