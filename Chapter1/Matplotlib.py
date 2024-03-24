import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 데이터 준비
x = np.arange(0, 6, 0.1)
print(x)

y = np.sin(x)

# draw graph
plt.plot(x, y)
plt.show()

# set dataset
y1 = np.sin(x)
y2 = np.cos(x)

# draw
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()

# image
img = imread('./pyplot.png')
plt.imshow(img)
plt.show()
