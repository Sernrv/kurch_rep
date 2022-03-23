import matplotlib.pyplot as plt
import numpy as np

wind, gr = plt.subplots()
x = np.linspace(-10, 10, 10)
y = np.sin(x)
y1 = np.cos(x)
gr.plot(y, y1)
plt.show()
