#! /usr/bin/env python3
"""
Demonstrate multiple linear regression, confidence interval, and prediction
interval with statsmodels
"""

import matplotlib.pyplot as plt
import statsmodels.api as sm
import datasense as ds
import pandas as pd


def main():
    output_url = "statsmodels_multiple_linear_regression.html"
    header_title = "Statsmodels multiple linear regression"
    header_id = "statsmodels-multiple-linear-regression"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    series_year = [
        2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017,
        2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016
    ]
    series_month = [
        12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 1
    ]
    series_interest_rate = [
        2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2, 2, 1.75,
        1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75
    ]
    series_unemployment_rate = [
        5.3, 5.3, 5.3, 5.3, 5.4, 5.6, 5.5, 5.5, 5.5, 5.6, 5.7, 5.9, 6, 5.9,
        5.8, 6.1, 6.2, 6.1, 6.1, 6.1, 5.9, 6.2, 6.2, 6.1
    ]
    series_index_price = [
        1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075,
        1047, 965, 943, 958, 971, 949, 884, 866, 876, 822, 704, 719
    ]
    x_column = ["interest_rate", "unemployment_rate"]
    prediction_column = "mean"
    y_column = "index_price"
    figsize = (8, 6)
    labellegendy1 = "Data"
    labellegendy2 = "Linear regression"
    graphnames = [
        "interest_rate_vs_index_price.svg",
        "unemployment_rate_vs_index_price.svg"
    ]
    df = pd.DataFrame(
        data={
            "year": series_year,
            "month": series_month,
            x_column[0]: series_interest_rate,
            x_column[1]: series_unemployment_rate,
            y_column: series_index_price
        }
    )
    df_predictions = ds.linear_regression(
        df=df,
        x_column=x_column,
        y_column=y_column,
        prediction_column=prediction_column
    )
    ds.style_graph()
    # need to figure out how to plot multiple regression graphs
    # for X, graphname in zip(x_column, graphnames):
    #     print(df_predictions[X])
    #     fig, ax = ds.plot_scatter_line_x_y1_y2(
    #         X=df_predictions[X],
    #         y1=df_predictions[y_column],
    #         y2=df_predictions[prediction_column],
    #         figsize=figsize,
    #         labellegendy1=labellegendy1,
    #         labellegendy2=labellegendy2
    #     )
    # ax.plot(
    #     df["interest_rate"],
    #     df[y_column],
    #     marker=".",
    #     linestyle="None",
    #     color="#0077bb"
    # )
    # ax.plot(
    #     df["interest_rate"],
    #     df[y_column],
    #     marker=".",
    #     linestyle="None",
    #     color="#cc3311"
    # )
    #     ax.set_title(
    #         label="Regression analysis",
    #         fontsize=15
    #         )
    #     ax.set_xlabel(
    #         xlabel="X axis label",
    #         fontsize=12
    #     )
    #     ax.set_ylabel(
    #         ylabel="Y axis label",
    #         fontsize=12
    #     )
    #     fig.savefig(
    #         fname=graphname,
    #         format="svg"
    #     )
    #     ds.html_figure(file_name=graphname)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
