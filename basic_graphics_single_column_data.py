#! /usr/bin/env python3
"""
Examples of graphics from a single column of data
"""

from pathlib import Path

from stemgraphic import stem_graphic as stg
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd
import numpy as np


def main():
    header_title = "Basic graphics using a single column of data"
    file_name = Path("basic_graphics_single_column_data.csv")
    output_url = "basic_graphics_single_column_data.html"
    header_id = "basic-graphics-single-column-data"
    file_name_histogram = Path("histogram.svg")
    file_name_box_plot = Path("box_plot.svg")
    subtitle = "Pretty graph"
    colour1 = "#0077bb"
    colour2 = "#33bbee"
    series_name = "y"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    df = ds.read_file(file_name=file_name)
    fig, ax = ds.plot_boxplot(
        series=df[series_name],
        notch=True,
        showmeans=True,
        remove_spines=True
    )
    box_plot_title = f"Box plot of {series_name}"
    ax.set_title(
        label=box_plot_title + "\n" + subtitle,
        fontsize=13
    )
    ax.set_ylabel(ylabel=series_name)
    fig.savefig(
        fname=file_name_box_plot,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_box_plot}")
    print("Maximum               :", df[series_name].max())
    print("Third quartile        :", df[series_name].quantile(.75))
    print("Median                :", df[series_name].median())
    print("Average               :", df[series_name].mean())
    print("First quartile        :", df[series_name].quantile(.25))
    print("Minimum               :", df[series_name].min())
    print(
        "Upper confidence value:",
        df[series_name].median() + 1.57 * (
                df[series_name].quantile(.75) - df[series_name].quantile(.25)
            ) /
        np.sqrt(df[series_name].count())
    )
    print(
        "Lower confidence value:",
        df[series_name].median() - 1.57 * (
                df[series_name].quantile(.75) - df[series_name].quantile(.25)
            ) /
        np.sqrt(df[series_name].count())
    )
    fig, ax = ds.plot_histogram(series=df[series_name])
    histogram_plot_title = f"Histogram of {series_name}"
    y_axis_label = "Count"
    ax.set_title(
        label=histogram_plot_title + "\n" + subtitle,
        fontsize=13
    )
    ax.set_ylabel(ylabel=y_axis_label)
    ax.set_xlabel(xlabel=series_name)
    fig.savefig(
        fname=file_name_histogram,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_histogram}")
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
