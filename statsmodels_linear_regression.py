#! /usr/bin/env python3
"""
Demonstrate linear regression, confidence interval, and prediction
interval with statsmodels
"""

import datasense as ds
import pandas as pd


def main():
    OUTPUT_URL = "statsmodels_linear_regression.html"
    HEADER_TITLE = "Statsmodels linear regression"
    HEADER_ID = "statsmodels-linear-regression"
    LABELLEGENDCI = "Confidence interval"
    LABELLEGENDPI = "Prediction interval"
    LABELLEGENDY2 = "Linear regression"
    TITLE = "Regression analysis"
    COLOUR_SHADING = "#888888"
    GRAPH_NAME = "y_vs_x.svg"
    XLABEL = "X axis label"
    YLABEL = "Y axis label"
    LABELLEGENDY1 = "Data"
    FIGSIZE = (8, 6)
    X_COLUMN = "x"
    Y_COLUMN = "y"
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    df = pd.DataFrame(
        data={
            X_COLUMN: [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            Y_COLUMN: [
                8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82,
                5.68
            ]
        }
    ).sort_values(by=X_COLUMN)
    (
        fitted_model, predictions, confidence_interval_lower,
        confidence_interval_upper, prediction_interval_lower,
        prediction_interval_upper
    ) = ds.linear_regression(
        X=df[X_COLUMN],
        y=df[Y_COLUMN],
    )
    ds.style_graph()
    fig, ax = ds.plot_scatter_line_x_y1_y2(
        X=df[X_COLUMN],
        y1=df[Y_COLUMN],
        y2=predictions,
        figsize=FIGSIZE,
        labellegendy1=LABELLEGENDY1,
        labellegendy2=LABELLEGENDY2
    )
    ax.fill_between(
        df[X_COLUMN],
        y1=confidence_interval_lower,
        y2=confidence_interval_upper,
        color=COLOUR_SHADING,
        alpha=0.4,
        label=LABELLEGENDCI
    )
    ax.fill_between(
        x=df[X_COLUMN],
        y1=prediction_interval_lower,
        y2=prediction_interval_upper,
        color=COLOUR_SHADING,
        alpha=0.2,
        label=LABELLEGENDPI
    )
    ax.set_title(
        label=TITLE,
        fontsize=15
    )
    ax.set_xlabel(
        xlabel=XLABEL,
        fontsize=12
    )
    ax.set_ylabel(
        ylabel=YLABEL,
        fontsize=12
    )
    ax.legend(
        loc="upper left",
        frameon=False
    )
    fig.savefig(
        fname=GRAPH_NAME,
        format="svg"
    )
    ds.html_figure(file_name=GRAPH_NAME)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
