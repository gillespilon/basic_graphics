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

from matplotlib.ticker import NullFormatter, NullLocator
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import statsmodels.api as sm
import datasense as ds
import pandas as pd
import numpy as np


figure_width_height = (8, 6)
colour1 = '#0077bb'
colour2 = '#33bbee'
colour3 = '#009988'
column_x, column_target, column_actual, column_predicted = (
    'Date',
    'TargetBalance',
    'ActualBalance',
    'Predicted'
)


chdir(Path(__file__).parent.__str__())


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
    data = regression(
        data=data,
        model='linear',
        column_x=column_x,
        column_actual=column_actual,
        column_predicted=column_predicted
    )
    ax = plot_three_lines(
        data,
        axis_title,
        x_axis_label,
        y_axis_label,
        figure_width_height
    )
    ds.despine(ax)
    ax.figure.savefig('actual_vs_target.svg', format='svg')
    ax.figure.savefig('actual_vs_target.png', format='png')


def plot_three_lines(
    data: pd.DataFrame,
    axis_title: str,
    x_axis_label: str,
    y_axis_label: str,
    figure_width_height: Tuple[int, int]
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
        color=colour1
    )
    ax.plot(
        data['Date'],
        data['ActualBalance'],
        label='ActualBalance',
        linestyle='-',
        color=colour2,
        marker='.'
    )
    ax.plot(
        data['Date'],
        data['Predicted'],
        label='Predicted',
        linestyle='-',
        color=colour3
    )
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%m'))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.legend(frameon=False)
    return ax


def regression(
    data: pd.DataFrame,
    model: str,
    column_x: str,
    column_actual: str,
    column_predicted: str
) -> pd.DataFrame:
    '''
    Estimate a linear regression line.

    Parameters
    ----------
    data : pd.DataFrame
        The dataframe.
    model : str
        The type of regression.
    column_x : str
        The absicssa of the model.
    column_actual : str
        The ordinate of the model.
    column_predicted : str
        The predicted ordinate of the model.

    Returns
    -------
    df : pd.DataFrame
        The dataframe with predicted results.
    '''
    data['DateDelta'] = (data['Date'] - data['Date']
                         .min())/np.timedelta64(1, 'D')
    model = sm.OLS(
        data['ActualBalance'],
        sm.add_constant(data['DateDelta']),
        missing='drop'
    ).fit()
    data['Predicted'] = model.fittedvalues
    return data


if __name__ == '__main__':
    main()
