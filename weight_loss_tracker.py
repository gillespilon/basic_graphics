#! /usr/bin/env python3

'''
Weight loss tracker using a line plot and fixed target line

time -f '%e' ./weight_loss_tracker.py
./weight_loss_tracker.py
'''

# TODO:
# - Confidence interval
# - Prediction interval

import pandas as pd
import matplotlib
import matplotlib.cm as cm
import matplotlib.axes as axes


c = cm.Paired.colors


matplotlib.use('Cairo')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    Used to enforce standard and *correct* style. There is only one x, and one
    y axis, left and bottom, therefore there should only be these axes.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


df = pd.read_csv('weight.csv',
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
ax.set_ylabel('Weight (kg)', fontweight='bold')
ax.autoscale(enable=True)
ax.set_title('Scatter Plot of Weight Loss',
             fontweight='bold')
despine(ax)


ax.figure.savefig('weight.svg',
                  format='svg')
