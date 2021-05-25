import mpmath as mpm
import plotly as pl
import plotly.express as px
from plotly.graph_objs import Scatter, Layout
import numpy as np


def f(p):
    z = p**2
    return z


X = np.arrange(0, 5, 0.1)
px.scatter(x=X, y=f(X)).show()
