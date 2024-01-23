#! /usr/bin/env python3
"""
It is a visualization of the cumulative effect of sequentially introduced
positive or negative values. These values can be time-based or category-based.

Based on code by Chris Moffitt:
https://pbpython.com/waterfall-chart.html

TODO: add code to read an Excel or csv file.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd
import numpy as np


def main():
    index = [
        "sales", "returns", "credit fees", "rebates", "late charges",
        "shipping"
    ]
    data = {"amount": [350000, -30000, -7500, -25000, 95000, -7000]}
    negative_colour = "red"
    positive_colour = "green"
    # trans is a DataFrame
    trans = pd.DataFrame(
        data=data,
        index=index
    )
    # blank is a DataFrame
    blank = trans["amount"].cumsum().shift(1).fillna(0)
    # total is a DataFrame
    total = trans.sum()["amount"]
    trans.loc["net"] = total
    blank.loc["net"] = total
    # step is a Series
    step = blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan
    blank.loc["net"] = 0
    # Plot with colors, keeping last bar green
    ax = trans.plot(
        kind="bar",
        stacked=True,
        bottom=blank,
        legend=None,
        fontsize=12
    )
    # Dynamically set bar colors based on values
    for i, p in enumerate(ax.patches):
        if trans.iloc[i]["amount"] > 0:
            p.set_facecolor(positive_colour)
        else:
            p.set_facecolor(negative_colour)
    # Change color of the last bar (index -1) to green
    # ax.patches contains a list of bar objects in the plot
    # ax.patches[-1] accesses the last bar in that list
    # last_bar = ax.patches[-1]
    # last_bar.set_facecolor('green')  # set desired color here
    ax.plot(
        step.index,
        step.values,
        "b",
        linewidth=0.5
    )
    ax.set_ylabel(
        ylabel="ylabel",
        weight="bold",
        fontsize=14
    )
    ax.set_xlabel(
        xlabel="xlabel",
        weight="bold",
        fontsize=14
    )
    ax.set_title(
        label="2014 Sales Waterfall",
        weight="bold",
        fontsize=14
    )
    ds.despine(ax=ax)
    ax.get_figure().savefig(
        "waterfall.svg",
        bbox_inches='tight'
    )
    plt.show()


if __name__ == "__main__":
    main()
