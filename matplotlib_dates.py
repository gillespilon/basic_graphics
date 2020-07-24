#! /usr/bin/env python3

'''
Explore plotting with matplotlib dates

time -f '%e' ./matplotlib_dates.py
./matplotlib_dates.py

References
https://docs.python.org/3/library/datetime.html#module-datetime
https://matplotlib.org/api/dates_api.html#matplotlib-date-format
'''


# TODO:
# fix two subplot function to accept four series instead of two dfs
# fix one subplot function to accept two series insteead of one df
# change call to graph functions so that they return ax and then add info


from typing import List, Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.axes as axes
from datetime import datetime
import matplotlib.cm as cm
import datasense as ds
import pandas as pd


def main():
    c = cm.Paired.colors
    pd.set_option('display.max_columns', 600)
    pd.set_option('display.max_rows', 600)
    figure_width_height = (8, 6)
    figure_title = 'Figure title'
    axis_title = 'Axis title'
    abscissa_label = 'abscissa'
    ordinate_label = 'ordinate'
    column_abscissa_datefloat_one = 'datefloats_one'
    column_abscissa_datetime_one = 'datetimes_one'
    column_abscissa_datefloat_two = 'datefloats_two'
    column_abscissa_datetime_two = 'datetimes_two'
    column_abscissa_one = 'abscissa_one'
    column_abscissa_two = 'abscissa_two'
    column_ordinate_one = 'ordinate_one'
    column_ordinate_two = 'ordinate_two'
    raw = {
        column_abscissa_one: [
            '2018-07-31', '2018-08-04', '2018-08-06', '2018-08-11',
            '2018-08-12', '2018-08-15', '2018-08-16', '2018-08-17',
            '2018-08-18', '2018-08-25', '2018-09-15'
        ],
        column_abscissa_two: [
            '2019-07-11', '2019-07-14', '2019-07-16', '2019-07-21',
            '2019-08-12', '2019-08-13', '2019-08-16', '2019-08-18',
            '2019-08-21', '2019-08-25', '2019-09-05'
        ],
        column_ordinate_one: [10, 15, 30, 35, 40, 45, 40, 30, 35, 50, 75],
        column_ordinate_two: [20, 35, 20, 15, 30, 45, 50, 40, 45, 50, 65]
    }
    data = pd.DataFrame(data=raw)
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    # Creates a list of datetime objects
    data[column_abscissa_datetime_one] =\
        str_to_datetime(data[column_abscissa_one])
    data[column_abscissa_datefloat_one] =\
        [mdates.date2num(date)
         for date in data[column_abscissa_datetime_one]]
    data[column_abscissa_datetime_two] =\
        str_to_datetime(data[column_abscissa_two])
    data[column_abscissa_datefloat_two] =\
        [mdates.date2num(date)
         for date in data[column_abscissa_datetime_two]]
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    print(
        f'Column data types\n'
        f'abscissa_one  : {data[column_abscissa_one].dtype}\n'
        f'abscissa_two  : {data[column_abscissa_two].dtype}\n'
        f'ordinate_one  : {data[column_ordinate_one].dtype}\n'
        f'ordinate_two  : {data[column_ordinate_two].dtype}\n'
        f'datetimes_one : {data[column_abscissa_datetime_one].dtype}\n'
        f'dates_one     : {data[column_abscissa_datefloat_one].dtype}\n'
        f'datetimes_two : {data[column_abscissa_datetime_two].dtype}\n'
        f'dates_two     : {data[column_abscissa_datefloat_two].dtype}\n'
    )
    # plot_line_two_subplots(
    #     data, column_abscissa, column_ordinate_one,
    #     file_name_graph, figure_width_height, figure_title, axis_title,
    #     abscissa_label, ordinate_label, c
    # )
    # Test line plot x y, smoothing None
    fig, ax = ds.plot_line_x_y(
        data[column_abscissa_datetime_one],
        data[column_ordinate_one]
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_line_plot.svg',
        abscissa_label,
        ordinate_label,
        c
    )
    # Test scatter plot x y, smoothing None
    fig, ax = ds.plot_scatter_x_y(
        data[column_abscissa_datetime_one],
        data[column_ordinate_one],
        figure_width_height
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_scatter_plot.svg',
        abscissa_label,
        ordinate_label,
        c,
        figure_title,
        axis_title,
    )
    # Test line plot x y, smoothing = 'natural_cubic_spline'
    fig, ax = ds.plot_line_x_y(
        data[column_abscissa_datetime_one],
        data[column_ordinate_one],
        smoothing='natural_cubic_spline',
        numknots=5
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_line_plot_smoothing.svg',
        abscissa_label,
        ordinate_label,
        c,
        axistitle=axis_title,
        figuretitle=None,
    )
    # Test scatter plot x y, smoothing = 'natural_cubic_spline'
    fig, ax = ds.plot_scatter_x_y(
        data[column_abscissa_datetime_one],
        data[column_ordinate_one],
        figure_width_height,
        smoothing='natural_cubic_spline',
        numknots=5
    )
    plot_pretty(
        fig,
        ax,
        'matplotlib_dates_scatter_plot_smoothing.svg',
        abscissa_label,
        ordinate_label,
        c,
        figure_title,
    )


def plot_pretty(
    fig: plt.figure,
    ax: axes.Axes,
    filenamegraph: str = None,
    abscissalabel: str = None,
    ordinatelabel: str = None,
    c: Tuple[Tuple[float]] = None,
    figuretitle: str = None,
    axistitle: str = None
) -> None:
    despine(ax)
    fig.suptitle(figuretitle, fontweight='bold', fontsize=16)
    ax.set_title(axistitle, fontweight='bold')
    ax.set_xlabel(abscissalabel, fontweight='bold')
    ax.set_ylabel(ordinatelabel, fontweight='bold')
    ax.figure.savefig(filenamegraph, format='svg')


def plot_line_two_subplots(
    dataframe: pd.DataFrame,
    columnx: str,
    columny: str,
    filenamegraph: str,
    figurewidthheight: Tuple[float],
    figuretitle: str,
    axistitle: str,
    xlabel: str,
    ylabel: str,
    c: Tuple[Tuple[float]]
) -> None:
    fig = plt.figure(figsize=figurewidthheight)
    loc = mdates.AutoDateLocator()
    fmt = mdates.AutoDateFormatter(loc)
    ax1 = fig.add_subplot(121)
    ax1.xaxis.set_major_locator(loc)
    ax1.xaxis.set_major_formatter(fmt)
    fig.autofmt_xdate()
    ax1.plot(
        dataframe[columnx],
        dataframe[columny],
        color=c[0]
    )
    despine(ax1)
    fig.suptitle(figuretitle, fontweight='bold', fontsize=16)
    ax1.set_title(axistitle, fontweight='bold')
    ax1.set_xlabel(xlabel, fontweight='bold')
    ax1.set_ylabel(ylabel, fontweight='bold')
    ax2 = fig.add_subplot(122)
    ax2.xaxis.set_major_locator(loc)
    ax2.xaxis.set_major_formatter(fmt)
    fig.autofmt_xdate()
    ax2.plot(
        dataframe[columnx],
        dataframe[columny],
        color=c[0]
    )
    despine(ax2)
    ax2.set_title(axistitle, fontweight='bold')
    ax2.set_xlabel(xlabel, fontweight='bold')
    ax2.set_ylabel(ylabel, fontweight='bold')
    fig.savefig(filenamegraph, format='svg')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.
    There is only one x axis, on the bottom,
    and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine]. set_visible(False)


def str_to_datetime(strings: List[str]) -> List[datetime]:
    '''
    Convert a list of 'YYYY-MM-DD' strings to a list of datetime objects.
    '''
    dates = []
    for date in strings:
        y, m, d = (int(x) for x in date.split('-'))
        date = datetime(y, m, d)
        dates.append(date)
    return dates


if __name__ == '__main__':
    main()
