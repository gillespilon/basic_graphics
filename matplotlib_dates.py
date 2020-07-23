#! /usr/bin/env python3

'''
Explore plotting with matplotlib dates

time -f '%e' ./matplotlib_dates.py
./matplotlib_dates.py

References
https://docs.python.org/3/library/datetime.html#module-datetime
https://matplotlib.org/api/dates_api.html#matplotlib-date-format
'''


from typing import List, Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.cm as cm
from datetime import datetime
import pandas as pd


def main():
    c = cm.Paired.colors
    file_name_graph = 'matplotlib_dates_line_plot.svg'
    figure_width_height = (8, 6)
    figure_title = 'Figure title'
    axis_title = 'Axis title'
    abscissa_label = 'abscissa'
    ordinate_label = 'ordinate'
    column_abscissa = 'dates'
    column_ordinate = 'ordinate'
    raw = {
        'abscissa': [
            '2018-07-31', '2018-08-04', '2018-08-06', '2018-08-11',
            '2018-08-12', '2018-08-15', '2018-08-16', '2018-08-17',
            '2018-08-18', '2018-08-25', '2018-09-15'
        ],
        'ordinate': [10, 15, 30, 35, 40, 45, 40, 30, 35, 50, 75]
    }
    data = pd.DataFrame(data=raw)
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    # Creates a list of datetime objects
    data['datetimes'] = str_to_datetime(data['abscissa'])
    data['dates'] = [mdates.date2num(date) for date in data['datetimes']]
    print(
        f'DataFrame:\n'
        f'{data}\n'
    )
    print(
        f'Column data types\n'
        f'abscissa : {data["abscissa"].dtype}\n'
        f'ordinate : {data["ordinate"].dtype}\n'
        f'datetimes: {data["datetimes"].dtype}\n'
        f'dates    : {data["dates"].dtype}\n'
    )
    plot_line(
        data, column_abscissa, column_ordinate,
        file_name_graph, figure_width_height, figure_title, axis_title,
        abscissa_label, ordinate_label, c
    )


def plot_line(
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
