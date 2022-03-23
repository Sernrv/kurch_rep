# %%
import sympy
from sympy import *

# %% plotting part
x = Symbol('x')
plot((sign(x), (x, -100, 100)), (sign(-x), (x, -100, 100)), (cos(x), (x, -100, 100)), line_color='red')

# %% plotting 3D
x, y = symbols('x y')
plotting.plot3d(x ** y, (x, -20, 20), (y, -20, 20))

# %% Equation part (solve)
x = S('x')
ex = sin(2 * x + 5) - sin(5 * x)
ex1 = sin(2 * x + 25) - sin(2 * x + 5)
sol = solve(ex)
res = float(N(sol[0]))
print(res)

# %% Equation part (solveset)
x = S('x')
ex = sin(x) - cos(x)
sol = solveset(ex, x)
print(sol)
a = sol.args[0].args[0]
print(a)
print(a(1))
print(float(a(1)))
print(a(2))
print(float(a(2)))

# %% Linear algebra part
A, B, C = symbols('A B C')
sol1 = linsolve([A + B + C, 8 * A + 4 * B + 6 * C - 8, 15 * A + 3 * B + 5 * C], (A, B, C))
print(sol1)

# %% limits part
x = S('x')
lim = limit((cos(x) - 1) / x, x, oo)
print('lim:', lim)
lim1 = limit(sign(x), x, 0, dir='-')
print('lim1:', lim1)

# %% Differential equation
x = S('x')
y = Function('y')
eq = Eq(diff(y(x), x, 2) - diff(y(x), x, 1), exp(x))
sol = dsolve(eq)
pprint(sol)