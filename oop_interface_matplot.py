import matplotlib.pyplot as plt
import numpy as np

X = np.arange(1, 15)
Y = X ** 2  # square of the X values
Z = (Y / 2) + 10

# this creates an empty canvas to plot on
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(X, Y, color='g', label='line 1')

ax.plot(X, Z, color="r", label='line2')

ax.set_title('Title of the plot', fontsize=15)
ax.set_xlabel('The X Factor', fontsize=15)
ax.set_ylabel('Label for Y axis', fontsize=15)

ax.legend()

plt.show()
