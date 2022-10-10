# 在气泡图中, 每个源泉的大小表示这个点的幅值
import numpy as np
import matplotlib.pyplot as plt

# 定义值的个数
num_vals = 40

# 生成随机的x值和y值
x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

# 在气泡图中定义每个点的面积值
max_radius = 25
area = np.pi * (max_radius * np.random.rand(num_vals)) ** 2

# 定义颜色
colors = np.random.random(num_vals)

# 画出数据点
plt.scatter(x, y, s=area, c=colors, alpha=1.0)

plt.show()