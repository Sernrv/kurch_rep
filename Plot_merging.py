import matplotlib.pyplot as plt
import numpy as np

n = 2
x = np.linspace(-10, 10, 100)
for j in range(n):
    plt.plot(x, np.sin(x), c='g', label='first')
    plt.plot(x, x, c='b', label='second')
    plt.legend()
plt.show()
