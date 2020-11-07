#! /usr/bin/env python3
"""
Cubic spline plot

This script has several functions:

- Estimate a cubic spline for abscissa, ordinate = integer, float
- Estimate a cubic spline for abscissa, ordinate = datetime, float
- Plot the raw data as a scatter plot
- Plot the cubic spline as a line plot

time -f '%e' ./cubic_spline.py
./cubic_spline.py
"""

from typing import Tuple

from matplotlib.ticker import NullFormatter, NullLocator
from matplotlib.dates import DateFormatter, DayLocator
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import datasense as ds
import pandas as pd


colour1 = '#0077bb'
colour2 = '#33bbee'
parser = '%Y-%m-%d %H:%M:%S'
file_name = [
    'raw_data_integer_float.csv',
    'raw_data_datetime_float.csv',
    'dataframe_small_datetime_integer.csv',
    'dataframe_small_integer_integer.csv'
]
abscissa_name = [
    'abscissa',
    'datetime',
    'datetime',
    'abscissa'
]
ordinate_name = [
    'ordinate',
    'observed',
    'observed',
    'ordinate'
]
ordinate_predicted_name = [
    'ordinate_predicted',
    'ordinate_predicted',
    'ordinate_predicted',
    'ordinate_predicted'
]
graph_file_name = [
    'cubic_spline_integer_float',
    'cubic_spline_datetime_float',
    'cubic_spline_dataframe_small_datetime_integer',
    'cubic_spline_dataframe_small_integer_integer'
]
date_time_parser = [None, parser, parser, None]
date_formatter = [None, '%m-%d', '%m-%d', None]
column_names_sort = [False, False, False, False]
figure_width_height = (8, 6)
x_axis_label = 'Abscissa'
y_axis_label = 'Ordinate'
axis_title = 'Cubic Spline'


def main():
    for (
        filename,
        abscissaname,
        ordinatename,
        ordinatepredictedname,
        datetimeparser,
        columnnamessort,
        dateformatter,
        graphfilename
    ) in zip(
        file_name,
        abscissa_name,
        ordinate_name,
        ordinate_predicted_name,
        date_time_parser,
        column_names_sort,
        date_formatter,
        graph_file_name
    ):
        data = ds.read_file(
            file_name=filename,
            parse_dates=[abscissaname],
            date_parser=datetimeparser,
            sort_columns=[abscissaname],
            sort_columns_bool=[columnnamessort]
        )
        data = ds.dataframe_info(
            df=data,
            file_in=filename
        )
        if datetimeparser is True:
            data[abscissaname] = pd.to_numeric(data[abscissaname])
            print('filename: ', filename)
            spline = ds.cubic_spline(
                df=data,
                abscissa=abscissaname,
                ordinate=ordinatename
            )
            data[ordinatepredictedname] = spline(data[abscissaname])
            data[abscissaname] = data[abscissaname].astype('datetime64[ns]')
        else:
            # data = data.sort_values(by=[abscissaname])
            print('filename: ', filename)
            spline = ds.cubic_spline(
                df=data,
                abscissa=abscissaname,
                ordinate=ordinatename
            )
            data[ordinatepredictedname] = spline(data[abscissaname])
        plot_graph(
            data,
            abscissaname,
            ordinatename,
            ordinatepredictedname,
            figure_width_height,
            dateformatter,
            graphfilename,
            axis_title,
            x_axis_label,
            y_axis_label
        )


def plot_graph(
    df: pd.DataFrame,
    columnx: str,
    columny: str,
    columnz: str,
    figurewidthheight: Tuple[int, int],
    dateformat: str,
    graphname: str,
    graphtitle: str,
    xaxislabel: str,
    yaxislabel: str
) -> None:
    fig = plt.figure(figsize=figurewidthheight)
    ax = fig.add_subplot(111)
    ax.plot(
        df[columnx],
        df[columny],
        marker='.',
        linestyle='',
        color=colour1
    )
    ax.plot(
        df[columnx],
        df[columnz],
        marker=None,
        linestyle='-',
        color=colour2
    )
    if dateformat:
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_minor_locator(NullLocator())
        ax.xaxis.set_major_formatter(DateFormatter(dateformat))
        ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_title(graphtitle, fontweight='bold')
    ax.set_xlabel(
        xlabel=xaxislabel,
        fontweight='bold'
    )
    ax.set_ylabel(
        ylabel=yaxislabel,
        fontweight='bold'
    )
    ds.despine(ax)
    fig.savefig(
        fname=f'{graphname}.svg',
        format='svg'
    )


if __name__ == '__main__':
    main()
