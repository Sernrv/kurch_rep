from Runge_Kutta import RGK


def Vel(tn, yn):
    return 9.81 * t


h = 0.00001
t = 0
H = 0
while t < 5:
    H += RGK(t, H, h, Vel)
    t += h
print(f'H: {H}', f't: {t}')
