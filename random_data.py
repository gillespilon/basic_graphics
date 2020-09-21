#! /usr/bin/env python3
"""
Create a series of random data for any distribution object.
"""

from scipy.stats import norm, uniform
import datasense as ds
import pandas as pd


def main():
    print('Random normal test')
    series_x = ds.random_data(
        distribution='norm',
        numrows=113
    )
    print(series_x.count())
    print(series_x.head())
    print('Random uniform test')
    series_x = ds.random_data(
        distribution='uniform',
        numrows=13
    )
    print(series_x.count())
    print(series_x.head())
    print('Random loggamma test')
    series_x = ds.random_data(
        distribution='loggamma',
        numrows=3
    )


if __name__ == '__main__':
    main()
