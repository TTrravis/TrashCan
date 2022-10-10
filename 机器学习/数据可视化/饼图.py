import numpy as np
import matplotlib.pyplot as plt

# 定义各标签和相应的值
data = {'Apple': 26,
        'Mango': 17,
        'Pineapple': 21,
        'Banana': 29,
        'Strawberry': 11}
# 定义可视化的颜色
colors = ['orange', 'lightgreen', 'lightblue', 'gold', 'cyan']

# 定义是否需要突出一部分
# explode = (0, 0, 0, 0, 0)
explode=(0, 0.2, 0, 0, 0)

# 画饼图
plt.pie(list(data.values()), explode=explode, labels=data.keys(),
        colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)

# 设置饼图的宽高比, "equal"表示我们希望它是圆形的
plt.axis('equal')
plt.show()
