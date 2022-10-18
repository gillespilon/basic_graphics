#! /usr/bin/env python3
"""
Examples of graphics from a single column of data
"""

from pathlib import Path

from stemgraphic import stem_graphic as stg
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd
import numpy as np


def main():
    header_title = "Basic graphics using a single column of data"
    file_name = Path("basic_graphics_single_column_data.csv")
    file_name_stemandleaf_plot = Path("stemandleafplot.svg")
    output_url = "basic_graphics_single_column_data.html"
    file_name_scatter_plot = Path("scatter_plot.svg")
    header_id = "basic-graphics-single-column-data"
    file_name_histogram = Path("histogram.svg")
    file_name_run_chart = Path("run_chart.svg")
    file_name_box_plot = Path("box_plot.svg")
    subtitle = "Pretty graph"
    colour1 = "#0077bb"
    colour2 = "#33bbee"
    series_name_y = "y"
    series_name_x = "x"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    df = ds.read_file(file_name=file_name)
    df[series_name_x] = df.index
    fig, ax = ds.plot_boxplot(
        series=df[series_name_y],
        notch=True,
        showmeans=True,
        remove_spines=True
    )
    box_plot_title = f"Box plot of {series_name_y}"
    ax.set_title(
        label=box_plot_title + "\n" + subtitle,
        fontsize=13
    )
    ax.set_ylabel(ylabel=series_name_y)
    fig.savefig(
        fname=file_name_box_plot,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_box_plot}")
    print("Maximum               :", df[series_name_y].max())
    print("Third quartile        :", df[series_name_y].quantile(.75))
    print("Median                :", df[series_name_y].median())
    print("Average               :", df[series_name_y].mean())
    print("First quartile        :", df[series_name_y].quantile(.25))
    print("Minimum               :", df[series_name_y].min())
    print(
        "Upper confidence value:",
        df[series_name_y].median() + 1.57 * (
                df[series_name_y].quantile(.75)
                - df[series_name_y].quantile(.25)
            ) /
        np.sqrt(df[series_name_y].count())
    )
    print(
        "Lower confidence value:",
        df[series_name_y].median() - 1.57 * (
                df[series_name_y].quantile(.75)
                - df[series_name_y].quantile(.25)
            ) /
        np.sqrt(df[series_name_y].count())
    )
    fig, ax = ds.plot_histogram(series=df[series_name_y])
    histogram_plot_title = f"Histogram of {series_name_y}"
    y_axis_label = "Count"
    ax.set_title(
        label=histogram_plot_title + "\n" + subtitle,
        fontsize=13
    )
    ax.set_ylabel(ylabel=y_axis_label)
    ax.set_xlabel(xlabel=series_name_y)
    fig.savefig(
        fname=file_name_histogram,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_histogram}")
    X = sm.add_constant(df[series_name_x])
    model = sm.OLS(endog=df[series_name_y], exog=X)
    results = model.fit()
    fig, ax = ds.plot_scatter_line_x_y1_y2(
        X=df[series_name_x],
        y1=df[series_name_y],
        y2=results.predict(),
        remove_spines=True
    )
    scatter_plot_title = f"Scatter plot of {series_name_y}"
    ax.set_title(
        label=scatter_plot_title + "\n" + subtitle,
        fontsize=13
    )
    ax.set_ylabel(ylabel=series_name_y)
    ax.set_xlabel(xlabel=series_name_x)
    fig.savefig(
        fname=file_name_scatter_plot,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_scatter_plot}")
    print("Coefficients of regression")
    print("Constant         :", results.params[0])
    print("Linear regression:", results.params[1])
    print()
    fig, ax = stg(df=df[series_name_y])
    stemandleaf_plot_title = f"Stem-and-leaf plot of {series_name_y}"
    ax.set_title(
        label=stemandleaf_plot_title,
        fontsize=13
    )
    fig.savefig(
        fname=file_name_stemandleaf_plot,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_stemandleaf_plot}")
    fig, ax = ds.plot_line_x_y(
        X=df[series_name_x],
        y=df[series_name_y],
        remove_spines=True
    )
    run_chart_title = f"Run chart of {series_name_y}"
    ax.set_title(
        label=run_chart_title,
        fontsize=13
    )
    ax.set_ylabel(ylabel=series_name_y)
    ax.set_xlabel(xlabel=series_name_x)
    fig.savefig(
        fname=file_name_run_chart,
        format="svg"
    )
    ds.html_figure(file_name=f"{file_name_run_chart}")
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
