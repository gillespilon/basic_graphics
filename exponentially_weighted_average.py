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

import matplotlib.axes as axes
import matplotlib.cm as cm
import datasense as ds
import webbrowser
import time
import sys


def main():
    start_time = time.time()
    global figure_width_height, c, date_time_parser
    file_names, graph_file_names, abscissa_names, ordinate_names,\
        ordinate_predicted_names, x_axis_label, y_axis_label, axis_title,\
        figure_width_height, column_names_sort, date_time_parser,\
        date_formatter, c, alpha_value, function, output_url,\
        header_title, header_id, parser = parameters()
    original_stdout = sys.stdout
    sys.stdout = open(output_url, 'w')
    ds.html_header(header_title, header_id)
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
        if datetimeparser == 'None':
            data = ds.read_file(
                filename=filename,
                abscissa=abscissaname,
                columnnamessort=columnnamessort
            )
        else:
            data = ds.read_file(
                filename=filename,
                abscissa=abscissaname,
                datetimeparser=parser,
                columnnamessort=columnnamessort
            )
        data[ordinatepredictedname] = data[ordinatename]\
            .ewm(alpha=alpha_value).mean()
        fig, ax = ds.plot_scatter_line_x_y1_y2(
            X=data[abscissaname],
            y1=data[ordinatename],
            y2=data[ordinatepredictedname],
            figuresize=figure_width_height
        )
        ax.set_title(axis_title, fontweight='bold')
        ax.set_xlabel(x_axis_label, fontweight='bold')
        ax.set_ylabel(y_axis_label, fontweight='bold')
        despine(ax)
        ax.figure.savefig(f'{graphfilename}.svg', format='svg')
        print(f'<p><img src="{graphfilename}.svg"/></p>')
    page_break()
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    summary(
        elapsedtime=elapsed_time,
        filenames=file_names,
        ordinatenames=ordinate_names,
        abscissanames=abscissa_names
    )
    ds.html_footer()
    sys.stdout.close()
    sys.stdout = original_stdout
    webbrowser.open_new_tab(output_url)


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
    str,
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
    parser = parameters['Other parameter values'][4]
    dateformatter = [None
                     if split.strip() == 'None' else
                     split.strip()
                     for unsplit
                     in parameters['Date formatter']
                     if str(unsplit) != 'nan'
                     for split
                     in unsplit.split(',')]
    c = cm.Paired.colors
    alphavalue = parameters['Other parameter values'][6]
    function = parameters['Other parameter values'][7]
    outputurl = parameters['Other parameter values'][8]
    headertitle = parameters['Other parameter values'][9]
    headerid = parameters['Other parameter values'][10]
    return (
        filenames, graphfilenames, abscissanames, ordinatenames,
        ordinatepredictednames, xaxislabel, yaxislabel, axistitle,
        figurewidthheight, columnnamessort, datetimeparser, dateformatter, c,
        alphavalue, function, outputurl, headertitle, headerid, parser
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


def page_break() -> None:
    '''
    Creates a page break for html output.
    '''

    print('<p style="page-break-after: always">')
    print('<p style="page-break-before: always">')


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
