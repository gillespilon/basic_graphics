#! /usr/bin/env python3

'''
Line plot, performance to target

time -f '%e' ./line_plot_actual_vs_target.py
./line_plot_actual_vs_target.py
'''

# TODO:
# - Confidence interval
# - Prediction interval

import pandas as pd
import matplotlib
import matplotlib.axes as axes
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.ticker import NullFormatter, NullLocator
pd.plotting.register_matplotlib_converters(explicit=True)


# c[0] c[1] ... c[11]
# See "paired" in "qualitative colormaps"
# https://matplotlib.org/tutorials/colors/colormaps.html
c = cm.Paired.colors


matplotlib.use('Cairo')


def despine(ax: axes.Axes) -> None:
    'Remove the top and right spines of a graph'
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


df = pd.read_csv('actual_vs_target.csv', parse_dates=['Date'])


figure_width_height = (8, 6)
axis_title = 'Plot of Savings Target vs Actual'
x_axis_label = 'Date'
y_axis_label = 'USD'
fig = plt.figure(figsize=figure_width_height)
ax = fig.add_subplot(111)
ax.plot(df['Date'], df['Target'], label='Target', linestyle='-', color=c[0])
ax.plot(df['Date'], df['Actual'], label='Actual', marker='o', linestyle='-',
        color=c[1])
ax.set_title(axis_title, fontweight='bold')
ax.set_xlabel(x_axis_label, fontweight='bold')
ax.set_ylabel(y_axis_label, fontweight='bold')
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_major_formatter(DateFormatter('%y-%m'))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.legend(frameon=False)
despine(ax)
ax.figure.savefig('target_vs_actual.svg', format='svg')
ax.figure.savefig('target_vs_actual.png', format='png')
