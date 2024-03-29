#! /usr/bin/env python3
"""
It is a visualization of the cumulative effect of sequentially introduced
positive or negative values. These values can be time-based or category-based.

Based on code by Chris Moffitt:
https://pbpython.com/waterfall-chart.html

See also:
https://matplotlib.org/stable/tutorials/artists.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html
"""

import matplotlib.artist as mpla
import matplotlib.pyplot as plt
import datasense as ds
import numpy as np


def main():
    TITLE = "2023-01 vs 2024-01 Margin Analysis"
    PATH_GRAPH_SVG = "waterfall_margin.svg"
    FILE_NAME = "waterfall_margin.xlsx"
    LAST_COLUMN = "2024-01 YTD"
    FIRST_BAR_COLOUR = "blue"
    LAST_BAR_COLOUR = "blue"
    POSITIVE_COLOUR = "blue"
    NEGATIVE_COLOUR = "red"
    GRID_ALPHA = 0.2
    YLIM_MIN = 15000
    YLIM_MAX = 40000
    FIGSIZE = (8, 6)
    FORMAT = "svg"
    df = ds.read_file(file_name=FILE_NAME)
    xlabel = df.columns[0]
    ylabel = df.columns[-1]
    df = df.set_index(df.columns[0])
    amount = df.columns[0]
    df_blank = df[amount].cumsum().shift(1).fillna(0)
    df_total = df.sum()[amount]
    df.loc[LAST_COLUMN] = df_total
    df_blank.loc[LAST_COLUMN] = df_total
    # step is a Series
    step = df_blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan
    df_blank.loc[LAST_COLUMN] = 0
    fig, ax = plt.subplots(figsize=FIGSIZE)
    x = df.index  # bar positions
    # create the waterfall chart, no need for a stacked argument
    ax.bar(x=x, height=df[amount], width=0.4, bottom=df_blank)
    ax.set_ylim(YLIM_MIN, YLIM_MAX)
    # set bar colors based on values
    for i, p in enumerate(ax.patches):
        if df.iloc[i][amount] > 0:
            p.set_facecolor(POSITIVE_COLOUR)
        else:
            p.set_facecolor(NEGATIVE_COLOUR)
    # Change color of the first and last bars
    # ax.patches contains a list of bar objects in the plot
    ax.patches[0].set_facecolor(FIRST_BAR_COLOUR)
    ax.patches[-1].set_facecolor(LAST_BAR_COLOUR)
    ax.plot(step.index, step.values, "b", linewidth=0.5)
    ax.tick_params(axis="x", labelsize=14,)
    ax.tick_params(axis="y", labelsize=14)
    ax.grid(visible=True, which="major", axis="y", alpha=GRID_ALPHA)
    ax.set_ylabel(ylabel=ylabel, weight="bold", fontsize=16)
    ax.set_xlabel(xlabel=xlabel, weight="bold", fontsize=16)
    ax.set_title(label=TITLE, weight="bold", fontsize=18)
    ds.despine(ax=ax)
    mpla.setp(
        obj=ax.get_xticklabels(),
        rotation=45,
        ha="right",
        rotation_mode="anchor"
    )
    fig.savefig(fname=PATH_GRAPH_SVG, format=FORMAT, bbox_inches="tight")
    print(df)


if __name__ == "__main__":
    main()
