#! /usr/bin/env python3
"""
Create a series of random data for any distribution object.
"""

from scipy.stats import norm
import pandas as pd


def main():
    series_x = random_data(numrows=113)
    print(series_x.count())
    print(series_x.head())


def random_data(
    numrows: int = 42
) -> pd.Series:
    """
    Create a series of random numbers from a standard normal distribution.

    Parameters
    ----------
    numrows : int = 42
        The number of rows to create.

    Returns
    -------
    pd.Series
        A pandas series of random normal numbers.
    """
    return pd.Series(norm.rvs(size=numrows))


if __name__ == '__main__':
    main()
