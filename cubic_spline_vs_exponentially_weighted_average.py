#! /usr/bin/env python3
"""
Plots to compare cubic spline vs exponentially weighted moving average fits
"""

from datetime import datetime

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import pandas as pd

date_time_parser = '%Y-%m-%d %H:%M:%S'
date_time_column = 'datetime'
observed_column = 'observed'
predicted_column = 'predicted'
colour1 = '#0077bb'
colour2 = '#cc3311'


def main():
    cs(
        'dataframe_small.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'cubic_spline'
    )
    cs(
        'dataframe_large.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'cubic_spline'
    )
    cs(
        'dataframe_large_clean.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'cubic_spline'
    )
    ewma(
        'dataframe_small.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'ewma'
    )
    ewma(
        'dataframe_large.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'ewma'
    )
    ewma(
        'dataframe_large_clean.csv',
        date_time_column,
        date_time_parser,
        observed_column,
        predicted_column,
        'ewma'
    )


def read_csv_file(
    filename: str,
    datecolumn: str,
    datetimeparser: str,
) -> pd.DataFrame:
    df = pd.read_csv(
         filename,
         parse_dates=[datecolumn],
         date_parser=lambda s: datetime.strptime(s, datetimeparser)
    )
    return df


def estimate_spline(
    df: pd.DataFrame,
    columnx: str,
    columny: str
) -> CubicSpline:
    '''
    Estimates the spline object for columnx, columny of a dataframe
    Requires that columnx, columny be integer or float
    Removes rows where there are missing values in columnx and columny
    Removes duplicate rows
    Sorts the dataframe by columnx in increasing order
    '''
    df = df.dropna(subset=[columnx, columny])
    df = df.sort_values(by=columnx, axis='rows', ascending=True)
    df = df.drop_duplicates(subset=columnx, keep='first')
    print('final dataframe', df.shape,
          'min', df[columny].min(),
          'max', df[columny].max())
    spline = CubicSpline(df[columnx], df[columny])
    return spline


def plot_graph(
    df: pd.DataFrame,
    columnx: str,
    columny: str,
    columnz: str,
    filename: str,
    graphname: str,
    graphtitle: str,
    graphsubtitle: str,
    yaxislabel: str,
    xaxislabel: str
) -> None:
    figszie = (8, 6)
    fig = plt.figure(figsize=figsize)
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
    ax.set_title(
        label=graphtitle + '\n' + graphsubtitle,
        
    )
    ax.set_xlabel(
        xlabel=xaxislabel,
        
    )
    ax.set_ylabel(
        ylabel=yaxislabel,
        
    )
    ds.despine(ax=ax)
    file = filename.strip('.csv')
    fig.savefig(
        fname=f'{graphname}_{file}.png',
        format='png'
    )


def cs(
    filename: str,
    datecolumn: str,
    datetimeparser: str,
    observedcolumn: str,
    predictedcolumn: str,
    graphname: str
) -> None:
    df = read_csv_file(filename, datecolumn, datetimeparser)
    print('initial dataframe', df.shape,
          'min', df[observedcolumn].min(),
          'max', df[observedcolumn].max())
    df[datecolumn] = pd.to_numeric(df[datecolumn])
    spline = estimate_spline(df, datecolumn, observedcolumn)
    df[predictedcolumn] = spline(df[datecolumn])
    df[datecolumn] = df[datecolumn].astype(dtype='datetime64[ns]')
    plot_graph(
        df,
        datecolumn,
        observedcolumn,
        predictedcolumn,
        filename,
        graphname,
        'Cubic Spline Fit',
        filename,
        observedcolumn,
        datecolumn
    )


def ewma(
    filename: str,
    datecolumn: str,
    datetimeparser: str,
    observedcolumn: str,
    predictedcolumn: str,
    graphname: str
) -> None:
    df = read_csv_file(filename, datecolumn, datetimeparser)
    print('initial & final', df.shape,
          'min', df[observedcolumn].min(),
          'max', df[observedcolumn].max())
    df[predictedcolumn] = df[observedcolumn].ewm(alpha=1).mean()
    plot_graph(
        df,
        datecolumn,
        observedcolumn,
        predictedcolumn,
        filename,
        graphname,
        'Exponentially Weighted Moving Average Fit',
        filename,
        observedcolumn,
        datecolumn
    )


if __name__ == '__main__':
    main()
