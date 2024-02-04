#! /usr/bin/env python3
"""
Create a waterfall chart. Arguments are passed using argparse.
"""

from pathlib import Path
import tkinter as tk
import argparse
import sys

import datasense as ds
import pandas as pd
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Create a waterfall chart")
    parser.add_argument(
        "-pf",
        "--path_or_file",
        type=Path,
        required=True,
        help="Provide a path or file of the .XLSX or .CSV file (required)",
    )
    parser.add_argument(
        "-lc",
        "--last_column",
        default="Net",
        type=str,
        required=False,
        help="Provide a string of the last column name (optional)",
    )
    parser.add_argument(
        "-xtlr",
        "--x_axis_tick_labels_rotation",
        default=45,
        type=float,
        required=False,
        help="Provide a float for the x axis tick labels rotation (optional)",
    )
    parser.add_argument(
        "-ymin",
        "--y_axis_min",
        default=None,
        type=float,
        required=False,
        help="Provide a minimum value for the y axis (optional)",
    )
    parser.add_argument(
        "-ymax",
        "--y_axis_max",
        default=None,
        type=float,
        required=False,
        help="Provide a maximum value for the y axis (optional)",
    )
    parser.add_argument(
        "-pc",
        "--positive_colour",
        default="green",
        type=str,
        required=False,
        help="Provide a string of the positive colour (optional)",
    )
    parser.add_argument(
        "-nc",
        "--negative_colour",
        default="red",
        type=str,
        required=False,
        help="Provide a string of the negative colour (optional)",
    )
    parser.add_argument(
        "-fcb",
        "--first_bar_colour",
        default="blue",
        type=str,
        required=False,
        help="Provide a string of the colour for the first bar (optional)",
    )
    parser.add_argument(
        "-lcb",
        "--last_bar_colour",
        default="blue",
        type=str,
        required=False,
        help="Provide a string of the colour for the last bar (optional)",
    )
    parser.add_argument(
        "-ga",
        "--grid_alpha",
        default=0.2,
        type=float,
        required=False,
        help="Provide a float for the grid alpha (0 <= value <= 1 optional)",
    )
    parser.add_argument(
        "-gf",
        "--graph_format",
        default="svg",
        choices=["svg", "png", "jpg"],
        type=str,
        required=False,
        help="Provide a string of the graph format (optional)",
    )
    parser.add_argument(
        "-gt",
        "--graph_title",
        default="Waterfall Chart",
        type=str,
        required=False,
        help="Provide a string of the graph title (optional)",
    )
    args = parser.parse_args()
    HEADER_TITLE = "Waterfall Report"
    HEADER_ID = "waterfall-report"
    OUTPUT_URL = "waterfall.html"
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL, header_title=HEADER_TITLE, header_id=HEADER_ID
    )
    df = ds.read_file(file_name=args.path_or_file)
    df = ds.waterfall(
        df=df,
        path_in=args.path_or_file,
        xticklabels_rotation=args.x_axis_tick_labels_rotation,
        last_column=args.last_column,
        ylim_min=args.y_axis_min,
        ylim_max=args.y_axis_max,
        positive_colour=args.positive_colour,
        negative_colour=args.negative_colour,
        first_bar_colour=args.first_bar_colour,
        last_bar_colour=args.last_bar_colour,
        grid_alpha=args.grid_alpha,
        graph_format=args.graph_format,
        title=args.graph_title,
    )
    print("data path or file    :", args.path_or_file)
    print("xticklabels rotation :", args.x_axis_tick_labels_rotation)
    print("Last column          :", args.last_column)
    print("y axis min           :", args.y_axis_min)
    print("y axis max           :", args.y_axis_max)
    print("positive colour      :", args.positive_colour)
    print("negative colour      :", args.negative_colour)
    print("first bar colour     :", args.first_bar_colour)
    print("last bar colour      :", args.last_bar_colour)
    print("grid alpha           :", args.grid_alpha)
    print("graph format         :", args.graph_format)
    print("graph title          :", args.graph_title)
    path_graph = args.path_or_file.with_suffix("." + args.graph_format)
    print("graph path or file   :", path_graph)
    print()
    print(df)
    print()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=OUTPUT_URL)


if __name__ == "__main__":
    main()
