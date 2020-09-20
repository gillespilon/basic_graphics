#! /usr/bin/env python3
"""
Demonstrate linear regression with statsmodels.
"""

from typing import Tuple

import matplotlib.pyplot as plt
from scipy.stats import norm
import statsmodels.api as sm
import pandas as pd


def main():
    series_x, series_y, df = random_data_norm()
    x = sm.add_constant(df['x'])
    y = df['y']
    model = sm.OLS(
        endog=y,
        exog=x,
        missing='drop'
    )
    results = model.fit()
    predicted = results.predict(x)
    results.summary()
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(
        series_x,
        series_y,
        marker='.',
        linestyle='None',
        color='#0077bb'
    )
    ax.plot(
        series_x,
        predicted,
        marker='None',
        linestyle='-',
        color='#cc3311'
    )
    ax.set_title(
        label='Regression analysis',
        fontsize=15,
        fontweight='bold'
    )
    ax.set_xlabel(
        xlabel='X axis label',
        fontsize=12,
        fontweight='bold'
    )
    ax.set_ylabel(
        ylabel='Y axis label',
        fontsize=12,
        fontweight='bold'
    )
    fig.savefig('y_vs_x.svg', format='svg')


def random_data_norm() -> Tuple[pd.Series, pd.Series, pd.DataFrame]:
    series_y = pd.Series(norm.rvs(size=42))
    series_x = pd.Series(norm.rvs(size=42))
    df = pd.DataFrame(
        {
            'x': series_x,
            'y': series_y
        }
    )
    return (series_x, series_y, df)


if __name__ == '__main__':
    main()
