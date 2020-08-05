#! /usr/bin/env python3

'''
Exponentially weighted average plot

This script has several functions:

- Estimate an exponentially weighted average for
    abscissa, ordinate = integer, float
- Estimate an exponentially weighted average for
    abscissa, ordinate = datetime, float
- Plot the raw data as a scatter plot
- Plot the exponentially weighted average as a line plot

time -f '%e' ./exponentially_weighted_average.py
./exponentially_weighted_average.py
'''


from typing import List, Tuple

from matplotlib.ticker import NullFormatter, NullLocator
from matplotlib.dates import DateFormatter, DayLocator
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.cm as cm
import datasense as ds
import pandas as pd


alpha_value = 1.0
function = 'mean'
figure_width_height = (8, 6)
x_axis_label = 'Abscissa'
y_axis_label = 'Ordinate'
axis_title = 'Exponentially Weighted Average'


def main():
    global figure_width_height, c
    file_names, graph_file_names, abscissa_names, ordinate_names,\
        ordinate_predicted_names, x_axis_label, y_axis_label, axis_title,\
        figure_width_height, column_names_sort, date_time_parser,\
        date_formatter, c = parameters()
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
        file_names,
        abscissa_names,
        ordinate_names,
        ordinate_predicted_names,
        date_time_parser,
        column_names_sort,
        date_formatter,
        graph_file_names
    ):
        data = ds.read_file(
            filename,
            abscissaname,
            datetimeparser,
            columnnamessort
        )
        data[ordinatepredictedname] = data[ordinatename]\
            .ewm(alpha=alpha_value).mean()
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


def parameters() -> (
    List[str],
    List[str],
    List[str],
    List[str],
    List[str],
    str,
    str,
    str,
    Tuple[float],
    List[bool],
    List[str],
    List[str],
    str
):
    '''
    Set parameters.
    '''

    parameters = ds.read_file(
        filename='exponentially_weighted_average_parameters.ods'
    )
    filenames = [x for x in parameters['File names'] if str(x) != 'nan']
    graphfilenames = [x for x in parameters['Graph file names']
                      if str(x) != 'nan']
    abscissanames = [x for x in parameters['Abscissa names']
                     if str(x) != 'nan']
    ordinatenames = [x for x in parameters['Ordinate names']
                     if str(x) != 'nan']
    ordinatepredictednames = [x for x in parameters['Ordinate predicted names']
                              if str(x) != 'nan']
    xaxislabel = parameters['Other parameter values'][0]
    yaxislabel = parameters['Other parameter values'][1]
    axistitle = parameters['Other parameter values'][2]
    figurewidthheight = eval(parameters['Other parameter values'][3])
    columnnamessort = [x for x in parameters['Column names sort']
                       if str(x) != 'nan']
    datetimeparser = [x for x in parameters['Date time parser']
                      if str(x) != 'nan']
    dateformatter = [None
                     if split.strip() == 'None' else
                     split.strip()
                     for unsplit
                     in parameters['Date formatter']
                     if str(unsplit) != 'nan'
                     for split
                     in unsplit.split(',')]
    c = cm.Paired.colors
    return (
        filenames, graphfilenames, abscissanames, ordinatenames,
        ordinatepredictednames, xaxislabel, yaxislabel, axistitle,
        figurewidthheight, columnnamessort, datetimeparser, dateformatter, c
    )


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


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
        color=c[1]
    )
    ax.plot(
        df[columnx],
        df[columnz],
        marker=None,
        linestyle='-',
        color=c[5]
    )
    if dateformat:
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_minor_locator(NullLocator())
        ax.xaxis.set_major_formatter(DateFormatter(dateformat))
        ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_title(graphtitle, fontweight='bold')
    ax.set_xlabel(xaxislabel, fontweight='bold')
    ax.set_ylabel(yaxislabel, fontweight='bold')
    despine(ax)
    ax.figure.savefig(f'{graphname}.svg', format='svg')


if __name__ == '__main__':
    main()
