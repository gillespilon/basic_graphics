#! /usr/bin/env python3
"""
Demonstrate multiple linear regression, confidence interval, and prediction
interval with statsmodels
"""

import datasense as ds
import pandas as pd


def main():
    OUTPUT_URL = "statsmodels_multiple_linear_regression.html"
    HEADER_TITLE = "Statsmodels multiple linear regression"
    HEADER_ID = "statsmodels-multiple-linear-regression"
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    SERIES_YEAR = [
        2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017,
        2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016
    ]
    SERIES_MONTH = [
        12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 1
    ]
    SERIES_INTEREST_RATE = [
        2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2, 2, 1.75,
        1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75
    ]
    SERIES_UNEMPLOYMENT_RATE = [
        5.3, 5.3, 5.3, 5.3, 5.4, 5.6, 5.5, 5.5, 5.5, 5.6, 5.7, 5.9, 6, 5.9,
        5.8, 6.1, 6.2, 6.1, 6.1, 6.1, 5.9, 6.2, 6.2, 6.1
    ]
    SERIES_INDEX_PRICE = [
        1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075,
        1047, 965, 943, 958, 971, 949, 884, 866, 876, 822, 704, 719
    ]
    X_COLUMN = ["interest_rate", "unemployment_rate"]
    Y_COLUMN = "index_price"
    df = pd.DataFrame(
        data={
            "year": SERIES_YEAR,
            "month": SERIES_MONTH,
            X_COLUMN[0]: SERIES_INTEREST_RATE,
            X_COLUMN[1]: SERIES_UNEMPLOYMENT_RATE,
            Y_COLUMN: SERIES_INDEX_PRICE
        }
    )
    (
        fitted_model, predictions, confidence_interval_lower,
        confidence_interval_upper, prediction_interval_lower,
        prediction_interval_upper
    ) = ds.linear_regression(
        X=df[X_COLUMN],
        y=df[Y_COLUMN],
        print_model_summary=True
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
