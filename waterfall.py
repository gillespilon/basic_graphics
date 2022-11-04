#! /usr/bin/env python3
"""
Waterfall chart, often used in finance

Based on code by Chris Moffitt:
https://pbpython.com/waterfall-chart.html
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
    ax = trans.plot(
        kind='bar',
        stacked=True,
        bottom=blank,
        legend=None,
        color="b",
        fontsize=12
    )
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
