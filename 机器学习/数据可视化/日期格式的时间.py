from datetime import date
from time import strptime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter

# ----------------csv2rec已被弃用-----------------


def csv2rec(filename):
    return np.recfromtxt(filename, dtype=None, delimiter=',', names=True, encoding='utf-8')

# 定义一个用于将日期格式化的类.


class DataFormatter(Formatter):
    def __init__(self, dates, date_format='%Y-%m-%d'):
        self.dates = dates
        self.dates_format = date_format

    # 提取给定时间的值
    def __call__(self, t, dates, postion=0):
        self.dates = dates
        index = int(round(t))
        if index >= len(str(self.dates)) or index < 0:
            return ''

        return (strptime(str(self.dates))[index]).strftime(self.dates_format)


if __name__ == '__main__':
    # 输入包含股价的csv文件
    input_file = cbook.get_sample_data('aapl.csv', asfileobj=False)

    # 将csv文件加载到numpy记录数组中
    data = csv2rec(input_file)

    # 提取这些值的子集
    data = data[-70:]

    # 创建一个格式化对象, 将其用日期数据初始化
    formatter = DataFormatter(date)

    # 定义X轴和Y轴
    # X
    x_vals = np.arange(len(data))

    # Y
    y_vals = data['Close']

    # 画出数据
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x_vals, y_vals, 'o-')
    fig.autofmt_xdate()
    plt.show()
