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

import datasense as ds


def main():
    chdir(Path(__file__).parent.resolve())  # required for cron
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
    data = ds.read_file(
        file_name=file_name_data,
        parse_dates=[column_x]
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
    ax.set_title(
        label=axis_title,

    )
    ax.set_xlabel(
        xlabel=x_axis_label,

    )
    ax.set_ylabel(
        ylabel=y_axis_label,

    )
    ax.legend(frameon=False)
    ds.despine(ax=ax)
    fig.savefig(
        fname=file_name_graph,
        format='svg'
    )


if __name__ == '__main__':
    main()
