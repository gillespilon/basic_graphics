# Basic graphics for a single  column of data

## In brevi

The purpose of this Jupyter notebook is to illustrate a basic notebook structure. The script reads a single-column file and calculates basic graphics. It progresses from quick-and-dirty code to pretty.

This Jupyter Notebook creates five graphs:

- Box plot
- Histogram
- Scatter plot
- Stem-and-leaf plot
- Run chart

## Data

Download the data file:

Download the data file:

- [basic_graphics_single_column_data.csv](https://drive.google.com/open?id=1N-5611OldWLD2hQwTDPOc1B0O_xxVoYO)

## Methodology

A box plot is drawn using pandas.plot.box(). A histogram is drawn using pandas.plot.hist(). A scatter plot is drawn using pandas.plot.scatter(). A regression line is estimated for the scatter plot using statsmodels.formula.api. A stem-and-leaf plot is drawn using stemgraphic.stem_graphic. A run chart is drawn using pandas.plot().

## References

- [matplotlib](https://matplotlib.org/api/pyplot_api.html)
- [numpy](https://docs.scipy.org/doc/numpy/reference/)
- [pandas API](https://pandas.pydata.org/pandas-docs/stable/api.html)
- [statsmodels](http://www.statsmodels.org/dev/example_formulas.html)
- [stemgraphic](http://stemgraphic.org/doc/index.html)
