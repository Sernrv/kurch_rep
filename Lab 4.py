import mpmath as mpm
import plotly as pl
<<<<<<< HEAD
import plotly.express as px
from plotly.graph_objs import Scatter, Layout
import numpy as np


def f(p):
    z = p**2
    return z


X = np.arrange(0, 5, 0.1)
px.scatter(x=X, y=f(X)).show()
=======
from numba import njit


@njit(fastmath=True, cache=True, parallel=True)
def rung(a, b):
    for i in range(b - a):
        y = list(map(mpm.cos(), i))
        return y


x1 = int(input())
x2 = int(input())
b = rung(x1, x2)
print(b)
>>>>>>> 1cdcb1c441dac142a2e9d8620612dcff77bec2c5
