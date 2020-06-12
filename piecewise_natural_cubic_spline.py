#! /usr/bin/env python3


'''
A piecewise natural cubic spline (cubic curves in the interior segments, linear
in the exterior segments) is used to interpolate points to fit the data while
smoothing out the noise. A large number of data are fitted with low-degree
polynomials, to eliminate excessive oscillations and non-convergence.

References

[Drury, Matthew. Basis Expansions](https://github.com/madrury/basis-expansions)

[Leal, Lois Anne. Numerical Interpolation: Natural Cubic Spline]
(https://towardsdatascience.com/numerical-interpolation-natural-cubic-spline
-52c1157b98ac)

[SAS/GRAPH SYMBOL Statement (INTERPOL=SM&lt;nn&gt;&lt;P&gt;&lt;S&gt;)]
(https://documentation.sas.com/?docsetId=graphref&docsetTarget=n0c0j84n1e2jz9n
1bhkn41o3v0d6.htm&docsetVersion=9.4&locale=en#p115cutvcmx2dln1cdo96duwmxru)

[Wikipedia. Smoothing spline](https://en.wikipedia.org/wiki/Smoothing_spline)

[Wikipedia. Spline (mathematics)]
(https://en.wikipedia.org/wiki/Spline_(mathematics))

time -f '%e' ./piecewise_natural_cubic_spline.py
time -f '%e' ./piecewise_natural_cubic_spline.py
./piecewise_natural_cubic_spline.py
'''


from multiprocessing import Pool
from typing import List, Tuple
import itertools
import basis_expansions as bsx
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Data set must not contain NaN, inf, or -inf
file_names = ['observed.csv', 'predicted.csv']
features = ['abscissa']
targets = ['ordinate']
figure_width_height = (6, 4)
x_axis_label = 'Abscissa'
y_axis_label = 'Ordinate'
axis_title = 'Piecewise natural cubic spline'
num_knots = [
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    # 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
    # 210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
]
c = cm.Paired.colors


def main():
    for file, target, feature in itertools.product(
        file_names, targets, features
    ):
        data = pd.read_csv(file)
        x = data[feature]
        y = data[target]
        min_val = min(x)
        max_val = max(x)
        t = ((x, y, min_val, max_val, file, target, feature, knot)
             for knot in num_knots)
        with Pool() as pool:
            for _ in pool.imap_unordered(plot_scatter_line, t):
                pass


def plot_scatter_line(t: Tuple[str, str]) -> None:
    x, y, min_val, max_val, file, target, feature, numknots = t
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
    ax.set_title(
        f'{axis_title}\n'
        f'file: {file} '
        f'column: {target}'
    )
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)
    despine(ax)
    ax.figure.savefig(
        f'spline_'
        f'{file.strip(".csv")}_'
        f'{target}_{feature}_'
        f'{numknots}.svg',
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
