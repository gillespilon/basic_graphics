#! /usr/bin/env python3
"""
"""

import matplotlib.pyplot as plt
from scipy.stats import norm
import statsmodels.api as sm
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")
series_y = pd.Series(norm.rvs(size=42))
series_x1 = pd.Series(norm.rvs(size=42))
series_x2 = pd.Series(norm.rvs(size=42))
df = pd.DataFrame(
    {
        'x1': series_x1,
        'x2': series_x2,
        'y': series_y
    }
)
x = sm.add_constant(df[['x1', 'x2']])
y = df['y']
model = sm.OLS(
    endog=y,
    exog=x,
    missing='drop'
)
results = model.fit()
df['y_predicted'] = results.predict(x)
results.summary()
df = df.sort_values(by=['x1'])
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(
    df['x1'],
    df['y'],
    marker='.',
    linestyle='None',
    color='#0077bb'
)
ax.plot(
    df['x1'],
    df['y_predicted'],
    marker='.',
    linestyle='None',
    color='#cc3311'
)
ax.set_title(
    label='Regression analysis',
    fontsize=15,
    fontweight='bold'
)
ax.set_xlabel(
    xlabel='X axis label',
    fontsize=12,
    fontweight='bold'
)
ax.set_ylabel(
    ylabel='Y axis label',
    fontsize=12,
    fontweight='bold'
)
fig.savefig('y_vs_x1.svg', format='svg')
df = df.sort_values(by=['x2'])
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(
    df['x2'],
    df['y'],
    marker='.',
    linestyle='None',
    color='#0077bb'
)
ax.plot(
    df['x2'],
    df['y_predicted'],
    marker='.',
    linestyle='None',
    color='#cc3311'
)
ax.set_title(
    label='Regression analysis',
    fontsize=15,
    fontweight='bold'
)
ax.set_xlabel(
    xlabel='X axis label',
    fontsize=12,
    fontweight='bold'
)
ax.set_ylabel(
    ylabel='Y axis label',
    fontsize=12,
    fontweight='bold'
fig.savefig('y_vs_x2.svg', format='svg')
