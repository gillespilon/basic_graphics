#! /usr/bin/env python3
"""
Create a series of random data for any distribution object.
"""

from scipy.stats import norm, uniform
import datasense as ds


def main():
    distribution = 'norm'
    print('Test 1')
    series_x = ds.random_data()
    print(series_x.describe())
    print('Test 2')
    series_x = ds.random_data(
        distribution=distribution
    )
    print(series_x.describe())
    print('Test 3')
    series_x = ds.random_data(
        size=34)
    print(series_x.describe())
    print('Test 4')
    series_x = ds.random_data(
        distribution=distribution,
        size=117,
        loc=53,
        scale=11
    )
    print(series_x.describe())
    distribution = 'uniform'
    print('Test 5')
    series_x = ds.random_data(
        distribution=distribution
    )
    print(series_x.describe())
    print('Test 6')
    series_x = ds.random_data(
        distribution=distribution,
        size=117,
        loc=13,
        scale=56
    )
    print(series_x.describe())


if __name__ == '__main__':
    main()
