#! /usr/bin/env python3

'''
Create line plots of actual and target for tracking weight loss.

time -f '%e' ./weight_loss_tracker.py
./weight_loss_tracker.py
'''

# TODO:
# - Confidence interval
# - Prediction interval

import matplotlib.axes as axes
import matplotlib.cm as cm
import datasense as ds
import pandas as pd


c = cm.Paired.colors
figure_width_height = (8, 6)
file_name_data, file_name_graph = (
    'weight.ods',
    'weight.svg'
)
column_x, column_target, column_actual = (
    'Date',
    'Target',
    'Actual'
)
x_axis_label, y_axis_label, axis_title = (
    'Date',
    'Weight (kg)',
    'Weight Loss'
)


def main():
    data = read_data(file_name_data)
    fig, ax = ds.plot_line_line_x_y1_y2(
              X=data[column_x],
              y1=data[column_target],
              y2=data[column_actual],
              figuresize=figure_width_height,
              labellegendy1=column_target,
              labellegendy2=column_actual
    )
    ax.set_title(label=axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.legend(frameon=False)
    despine(ax)
    ax.figure.savefig(file_name_graph, format='svg')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def read_data(filename: str) -> pd.DataFrame:
    '''
    Read the data into a dataframe.

    Parameters:
        filename    : str

    Returns:
        data        : pd.DataFrame
    '''
    data = pd.read_excel(
        filename,
        engine='odf',
        parse_dates=['Date']
    )
    return data


if __name__ == '__main__':
    main()
