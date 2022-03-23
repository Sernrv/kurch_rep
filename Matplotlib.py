import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

fig = plt.figure('Test')
# fig, axes = plt.figure('Test')
# fig, axes = figure('test'), plt.subplots(1, 4)
fig.add_subplot(141)
fig.add_subplot(142)
# fig.add_subplot(234)
# fig.add_subplot(235)
fig.suptitle('Subtitle')
fig.set_label('Test')

# plt.figure('Figure')

# axes[0].set_title('Title_1')
# axes[1].set_title('Title_2')
# axes[2].set_title('title_3')
# axes[3].set_title('title_4')

plt.show()
