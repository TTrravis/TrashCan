import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成一个空白图像
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# 定义应该生成的值的个数
n = 250

# 生成一个lamda函数来生成给定范围的值
f = lambda minval, maxval, n: minval+(maxval-minval)*np.random.rand(n)

# 使用这个函数生成X,Y,Z值
x_vals = f(15, 41, n)
y_vals = f(-10, 70, n)
z_vals = f(-52, -37, n)

# 画出
ax.scatter(x_vals, y_vals, z_vals, s=80, c='g', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

