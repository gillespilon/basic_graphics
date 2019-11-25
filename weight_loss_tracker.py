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
from matplotlib.dates import DateFormatter, DayLocator
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import NullLocator


c = cm.Paired.colors
fighw = (8, 6)
fig_title = 'Weight loss analysis'


matplotlib.use('Cairo')


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    Used to enforce standard and *correct* style. There is only one x, and one
    y axis, left and bottom, therefore there should only be these axes.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


# df = pd.read_csv('weight.csv',
#                  parse_dates=True,
#                  index_col='Date')


df = pd.read_csv('weight.csv',
                 parse_dates=['Date'])


print(df.head())
print(df.dtypes)


ax = df.plot.line(y='Target',
                  legend=False,
                  color=c[0])
df.plot.line(y='Actual',
             ax=ax,
             style='.',
             figsize=(12, 6),
             legend=False,
             color=c[1])
ax.set_xlabel('Date', fontweight='bold')
ax.set_ylabel('Weight (kg)', fontweight='bold')
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_formatter(NullFormatter())
ax.xaxis.set_major_formatter(DateFormatter('%d'))
ax.autoscale(enable=True)
ax.set_title('Scatter Plot of Weight Loss',
             fontweight='bold')
despine(ax)


ax.figure.savefig('weight.svg',
                  format='svg')

if __name__ == '__main__':
    pass
    # df = read_data()
    # plot_weight(df)
