import numpy as np
import matplotlib.pylab as plt


def step_function_1(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function_2(x):
    y = x > 0
    return y.astype(np.int)


def step_function(x):
    return np.array(x > 0, dtype=np.int64)


x1 = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x1)

plt.plot(x1, y1)
plt.ylim(-.1, 1.1)
plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


y2 = sigmoid(x1)

plt.plot(x1, y2)
plt.ylim(-.1, 1.1)
plt.show()