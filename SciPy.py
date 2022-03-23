from scipy.integrate import *
from numpy import *


def dfdx(x, t):
    return x ** 2


t = arange(0, 1, 0.01)
integral = ode(dfdx).set_integrator('dopri5')
# integral = ode(dfdx).set_integrator('dop853')
# integral = ode(dfdx).set_integrator('zvode')
# integral = ode(dfdx).set_integrator('vode')
integral.set_initial_value(0, 0)
# for i in t:
#     res = integral.integrate(i)
#     print(res)
while integral.successful() and integral.t < 1:
    res = integral.integrate(integral.t + 0.01)
    # print(integral.integrate(integral.t + 0.01))
print(float(res))
# print(res)