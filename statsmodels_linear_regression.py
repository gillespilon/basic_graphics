#! /usr/bin/env python3
"""
Demonstrate linear regression, confidence interval, and prediction
interval with statsmodels
"""

import matplotlib.pyplot as plt
import statsmodels.api as sm
import datasense as ds
import pandas as pd
import numpy as np


def main():
    output_url = "statsmodels_linear_regression.html"
    header_title = "Statsmodels linear regression"
    lower_ci_column = "lower_confidence_interval"
    upper_ci_column = "upper_confidence_interval"
    lower_pi_column = "lower_prediction_interval"
    upper_pi_column = "upper_prediction_interval"
    header_id = "statsmodels-linear-regression"
    prediction_column = "predicted"
    title = "Regression analysis"
    graphname = "y_vs_x.svg"
    xlabel = "X axis label"
    ylabel = "Y axis label"
    colour1 = "#0077bb"
    colour2 = "#cc3311"
    colour3 = "#888888"
    colerror = "error"
    x_column = "x"
    y_column = "y"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    print("<pre style='white-space: pre-wrap;'>")
    data = {
        x_column: [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        y_column: [
            8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68
        ]
    }
    df = pd.DataFrame(data=data)
    x = sm.add_constant(data=df[x_column])
    y = df[y_column]
    model = sm.OLS(
        endog=y,
        exog=x,
        missing="drop"
    )
    results = model.fit(
        method="pinv",
        cov_type="nonrobust"
    )
    df[prediction_column] = results.predict(exog=x)
    print(results.summary())
    print("</pre>")
    df[colerror] = df[x_column].std() * np.sqrt(
        1 / len(df[x_column]) + (df[x_column] - df[x_column].mean()) ** 2 /
        np.sum((df[x_column] - df[x_column].mean()) ** 2)
    )
    df[lower_ci_column] = df[prediction_column] - df[colerror]
    df[upper_ci_column] = df[prediction_column] + df[colerror]
    sum_squared_errors = (df[colerror] ** 2).sum()
    std_deviation_prediction = np.sqrt(
        1 / (len(df[y_column]) - 2) * sum_squared_errors
    )
    prediction_interval = 1.96 * std_deviation_prediction
    df[lower_pi_column] = df[prediction_column] - prediction_interval
    df[upper_pi_column] = df[prediction_column] + prediction_interval
    df = df.sort_values(by=x_column)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(
        df[x_column],
        df[y_column],
        marker=".",
        linestyle="None",
        color=colour1
    )
    ax.plot(
        df[x_column],
        df[prediction_column],
        marker="None",
        linestyle="-",
        color=colour2
    )
    ax.fill_between(
        x=df[x_column],
        y1=df[lower_ci_column],
        y2=df[upper_ci_column],
        color=colour3,
        alpha=0.4
    )
    ax.fill_between(
        x=df[x_column],
        y1=df[lower_pi_column],
        y2=df[upper_pi_column],
        color=colour3,
        alpha=0.2
    )
    ax.set_title(
        label=title,
        fontsize=15,

    )
    ax.set_xlabel(
        xlabel=xlabel,
        fontsize=12,

    )
    ax.set_ylabel(
        ylabel=ylabel,
        fontsize=12,

    )
    ds.despine(ax=ax)
    fig.savefig(
        fname=graphname,
        format="svg"
    )
    ds.html_figure(file_name=graphname)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
