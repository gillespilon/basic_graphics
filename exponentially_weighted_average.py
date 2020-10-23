#! /usr/bin/env python3
"""
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
"""

from typing import List, Tuple
import time

import matplotlib.axes as axes
import datasense as ds


def main():
    start_time = time.time()
    global figsize, date_time_parser
    file_names, graph_file_names, abscissa_names, ordinate_names,\
        ordinate_predicted_names, x_axis_label, y_axis_label, axis_title,\
        figsize, column_names_sort, date_time_parser,\
        date_formatter, alpha_value, function, output_url,\
        header_title, header_id, parser = parameters()
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    print('<pre style="white-space: pre-wrap;">')
    for (
        file_name,
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
        if datetimeparser == 'None':
            data = ds.read_file(
                file_name=file_name,
                # parse_dates=abscissaname,
                sort_columns=columnnamessort,
                sort_columns_bool=True
            )
        else:
            data = ds.read_file(
                file_name=file_name,
                # parse_dates=[abscissaname],
                # date_parser=parser,
                sort_columns=columnnamessort,
                sort_columns_bool=True
            )
        data[ordinatepredictedname] = data[ordinatename]\
            .ewm(alpha=alpha_value).mean()
        fig, ax = ds.plot_scatter_line_x_y1_y2(
            X=data[abscissaname],
            y1=data[ordinatename],
            y2=data[ordinatepredictedname],
            figsize=figsize
        )
        ax.set_title(axis_title, fontweight='bold')
        ax.set_xlabel(x_axis_label, fontweight='bold')
        ax.set_ylabel(y_axis_label, fontweight='bold')
        despine(ax)
        fig.savefig(
            fname=f'{graphfilename}.svg',
            format='svg'
        )
        print(f'<p><img src="{graphfilename}.svg"/></p>')
    ds.page_break()
    stop_time = time.time()
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time,
        read_file_names=file_names,
        targets=ordinate_names,
        features=abscissa_names
    )
    print('</pre>')
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
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
    float,
    str,
    str,
    str,
    str,
    str
):
    '''
    Set parameters.
    '''

    parameters = ds.read_file(
        file_name='exponentially_weighted_average_parameters.ods'
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
    parser = parameters['Other parameter values'][4]
    dateformatter = [None
                     if split.strip() == 'None' else
                     split.strip()
                     for unsplit
                     in parameters['Date formatter']
                     if str(unsplit) != 'nan'
                     for split
                     in unsplit.split(',')]
    alphavalue = parameters['Other parameter values'][6]
    function = parameters['Other parameter values'][7]
    output_url = parameters['Other parameter values'][8]
    header_title = parameters['Other parameter values'][9]
    header_id = parameters['Other parameter values'][10]
    return (
        filenames, graphfilenames, abscissanames, ordinatenames,
        ordinatepredictednames, xaxislabel, yaxislabel, axistitle,
        figurewidthheight, columnnamessort, datetimeparser, dateformatter,
        alphavalue, function, output_url, header_title, header_id, parser
    )


def despine(ax: axes.Axes) -> None:
    """
    Remove the top and right spines of a graph.

    Parameters
    ----------
    ax : axes.Axes

    Example
    -------
    >>> despine(ax)
    """
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def summary(
    elapsedtime: float,
    filenames: List[str],
    ordinatenames: List[str],
    abscissanames: List[str]
) -> None:
    '''
    Print report summary.
    '''

    print('<h1>Report summary</h1>')
    print(f'Execution time : {elapsedtime:.3f} s')
    print(f'Files read     : {filenames}')
    print(f'Orindates      : {ordinatenames}')
    print(f'Abscissas      : {abscissanames}')


if __name__ == '__main__':
    main()
