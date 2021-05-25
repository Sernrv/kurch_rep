import mpmath as mpm
import plotly as pl
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