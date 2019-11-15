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
import matplotlib.cm as cm
import matplotlib.axes as axes


c = cm.Paired.colors
# c[0] c[1] ... c[11]
# See "paired" in "qualitative colormaps"
# https://matplotlib.org/tutorials/colors/colormaps.html


matplotlib.use('Cairo')


def despine(ax: axes.Axes) -> None:
    'Remove the top and right spines of a graph'
    for spine in 'right', 'top':
#         ax.spines[spine].set_visible(False)
        ax.spines[spine].set_visible(False)


df = pd.read_csv('actual_vs_target.csv',
                 parse_dates=True,
                 index_col='Date')


df.head()


ax = df.plot.line(y='Target',
                  legend=False,
                  color=c[0])
df.plot.line(y='Actual',
             legend=False,
             style='.',
             color=c[1],
             figsize=(9, 6),
             ax=ax)
ax.set_xlabel('Date', fontweight='bold')
ax.set_ylabel('$', fontweight='bold')
ax.autoscale(enable=True)
ax.set_title('Scatter Plot of Target vs Actual',
             fontweight='bold')
despine(ax)


ax.figure.savefig('target_vs_actual.svg',
                  format='svg')