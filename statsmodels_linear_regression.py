#! /usr/bin/env python3
"""
Demonstrate linear regression with statsmodels.
"""

import matplotlib.pyplot as plt
import statsmodels.api as sm
import datasense as ds
import pandas as pd


output_url = 'statsmodels_linear_regression.html'
header_title = 'Statsmodels linear regression'
header_id = 'statsmodels-linear-regression'


def main():
    original_stdout = ds.html_begin(
        outputurl=output_url,
        headertitle=header_title,
        headerid=header_id
    )
    print('<pre>')
    df = pd.DataFrame(
        {
            'x': ds.random_data(),
            'y': ds.random_data()
        }
    )
    x = sm.add_constant(df['x'])
    y = df['y']
    model = sm.OLS(
        endog=y,
        exog=x,
        missing='drop'
    )
    results = model.fit()
    df['predicted'] = results.predict(x)
    print(results.summary())
    print('</pre>')
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(
        df['x'],
        df['y'],
        marker='.',
        linestyle='None',
        color='#0077bb'
    )
    ax.plot(
        df['x'],
        df['predicted'],
        marker='None',
        linestyle='-',
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
    fig.savefig('y_vs_x.svg', format='svg')
    print('<p><img src="y_vs_x.svg" alt="y_vs_x.svg"/></p>')
    ds.html_end(
        originalstdout=original_stdout,
        outputurl=output_url
    )


if __name__ == '__main__':
    main()
