#! /usr/bin/env python3

"""
Line plots of actual and target data, and regression line of actual data.

- Line plot of target value (y) versus date (x)
- Line plot of actual value (y) versus date (x)
- Line plot of predicted value (y) versus date (x) using linear regression

time -f "%e" ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
"""

from pathlib import Path
from os import chdir

import statsmodels.api as sm
import datasense as ds
import pandas as pd
import numpy as np


def main():
    x_axis_label, y_axis_label, axis_title, figsize = (
        "Date",
        "USD",
        "Savings Target vs Actual",
        (8, 6)
    )
    column_x, column_target, column_actual, column_predicted = (
        "Date",
        "TargetBalance",
        "ActualBalance",
        "Predicted"
    )
    file_name_data, file_name_graph = (
        "actual_vs_target.ods",
        "actual_vs_target.svg"
    )
    chdir(Path(__file__).parent.resolve())  # required for cron
    data = ds.read_file(
        file_name=file_name_data,
        parse_dates=[column_x]
    )
    data = regression(
        data=data,
        model="linear",
        column_x=column_x,
        column_actual=column_actual,
        column_predicted=column_predicted
    )
    fig, ax = ds.plot_line_line_line_x_y1_y2_y3(
        X=data[column_x],
        y1=data[column_target],
        y2=data[column_actual],
        y3=data[column_predicted],
        figsize=figsize,
        labellegendy1=column_target,
        labellegendy2=column_actual,
        labellegendy3=column_predicted
    )
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
    ds.format_dates(fig, ax)
    ds.despine(ax=ax)
    fig.savefig(
        fname=file_name_graph,
        format="svg"
    )


def regression(
    data: pd.DataFrame,
    model: str,
    column_x: str,
    column_actual: str,
    column_predicted: str
) -> pd.DataFrame:
    """
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
    """
    data["DateDelta"] = (data["Date"] - data["Date"]
                         .min())/np.timedelta64(1, "D")
    model = sm.OLS(
        data["ActualBalance"],
        sm.add_constant(data["DateDelta"]),
        missing="drop"
    ).fit()
    data["Predicted"] = model.fittedvalues
    return data


if __name__ == "__main__":
    main()
