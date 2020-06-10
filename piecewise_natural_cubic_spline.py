#! /usr/bin/env python3


'''
time -f '%e' ./piecewise_natural_cubic_spline.py
time -f '%e' ./piecewise_natural_cubic_spline.py
./piecewise_natural_cubic_spline.py
'''


from multiprocessing import Pool
from typing import List, Tuple
import basis_expansions as bsx
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Data set must not contain NaN, inf, or -inf
file_name = ['observed.csv', 'predicted.csv']
figure_width_height = (6, 4)
x_axis_label = 'Abscissa'
y_axis_label = 'Ordinate'
axis_title = 'Piecewise natural cubic spline'
# Change this list to try different amounts of smoothing
num_knots = [
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
    210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
]
c = cm.Paired.colors


def main():
    for file in file_name:
        data = pd.read_csv(file)
        x = data['abscissa']
        y = data['ordinate']
        min_val = min(x)
        max_val = max(x)
        t = ((x, y, min_val, max_val, file, knot) for knot in num_knots)
        with Pool() as pool:
            for _ in pool.imap_unordered(plot_cubic_thing, t):
                pass


def plot_cubic_thing(t: Tuple[str, str]) -> None:
    x, y, min_val, max_val, filename, numknots = t
    model = get_natural_cubic_spline(
        x, y, min_val, max_val, n_knots=numknots
    )
    fig = plt.figure(figsize=figure_width_height)
    ax = fig.add_subplot(111)
    ax.plot(x, y, ls='', marker='.', color=c[1], alpha=0.20)
    ax.plot(
        x, model.predict(x), marker='', color=c[5],
        label=f'number knots = {numknots}'
    )
    ax.legend(frameon=False, loc='best')
    ax.set_title(axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    despine(ax)
    ax.figure.savefig(
        f'natural_cubic_spline_'
        f'{filename.strip(".csv")}_{numknots}.svg',
        format='svg'
    )


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def get_natural_cubic_spline(
    x: pd.Series,
    y: pd.Series,
    minval: int = None,
    maxval: int = None,
    n_knots: int = None,
    knots: List[int] = None
):
    '''
    Natural cubic spline model

    For the knots, give (a) `knots` (as an array) or
    (b) minval, maxval and n_knots.

    If the knots are not directly specified, the resulting knots are
    equally-spaced within the *interior* of (max, min).  That is,
    the endpoints are *not* included as knots.

    Parameters
    ----------
    x: pd.Series
    y: pd.Series
    minval: minimum of interval containing the knots.
    maxval: maximum of the interval containing the knots.
    n_knots: the number of knots to create.
    knots: the knots.

    Returns
    --------
    model: a model object
        The returned model will have following method:
        - predict(x):
            x is a numpy array. This will return the predicted
            y-values.
    '''
    if knots:
        spline = bsx.NaturalCubicSpline(knots=knots)
    else:
        spline = bsx.NaturalCubicSpline(
            max=maxval, min=minval, n_knots=n_knots
        )
    p = Pipeline([
        ('natural_cubic_spline', spline),
        ('linear_regression', LinearRegression(fit_intercept=True))
    ])
    p.fit(x, y)
    return p


if __name__ == '__main__':
    main()
