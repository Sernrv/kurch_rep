def RGK(xn, yn, h, f):
    k1 = h * f(xn, yn)
    k2 = h * f(xn + h / 2, yn + k1 / 2)
    k3 = h * f(xn + h / 2, yn + k2 / 2)
    k4 = h * f(xn + h, yn + k3)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6

