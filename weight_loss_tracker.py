#! /usr/bin/env python3
"""
Create line plots of actual and target for tracking weight loss.

time -f '%e' ./weight_loss_tracker.py
./weight_loss_tracker.py
"""

# TODO:
# - Confidence interval
# - Prediction interval

from pathlib import Path
from os import chdir

import matplotlib.axes as axes
import datasense as ds

figure_width_height = (15, 7)
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


chdir(Path(__file__).parent.__str__())


def main():
    data = ds.read_file(
        file_name=file_name_data,
        parse_dates=column_x
    )
    fig, ax = ds.plot_line_line_x_y1_y2(
              X=data[column_x],
              y1=data[column_actual],
              y2=data[column_target],
              figsize=figure_width_height,
              labellegendy1=column_actual,
              labellegendy2=column_target,
              marker2=None,
              linestyle1='None',
    )
    ax.set_title(label=axis_title, fontweight='bold')
    ax.set_xlabel(x_axis_label, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.legend(frameon=False)
    ds.despine(ax)
    fig.savefig(
        fname=file_name_graph,
        format='svg'
    )


if __name__ == '__main__':
    main()
