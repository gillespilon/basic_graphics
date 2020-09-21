#! /usr/bin/env python3
"""
Create a series of random data for any distribution object.
"""

from scipy.stats import norm, uniform
import pandas as pd


def main():
    print('Random normal test')
    series_x = random_data(
        distribution='norm',
        numrows=113
    )
    print(series_x.count())
    print(series_x.head())
    print('Random uniform test')
    series_x = random_data(
        distribution='uniform',
        numrows=13
    )
    print(series_x.count())
    print(series_x.head())
    print('Random loggamma test')
    series_x = random_data(
        distribution='loggamma',
        numrows=3
    )


def random_data(
    distribution: str = 'norm',
    numrows: int = 42
) -> pd.Series:
    """
    Create a series of random numbers from a distribution.

    Parameters
    ----------
    distribution : str = 'norm'
        A scipy.stats distribution.
    numrows : int = 42
        The number of rows to create.

    Returns
    -------
    pd.Series
        A pandas series of random numbers.
    """
    distribution_list_one = ['norm', 'uniform']
    if distribution in distribution_list_one:
        series = pd.Series(eval(distribution).rvs(size=numrows))
    else:
        print(
            f'Random distribution instance {distribution} is not implemented '
            'in datasense.'
            )
        exit()
    return series


if __name__ == '__main__':
    main()
