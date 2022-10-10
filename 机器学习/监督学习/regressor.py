import sys
import numpy as np
from sklearn import linear_model  # 创建线性回归器对象
import matplotlib.pyplot as plt
import pickle as pk
import sklearn.metrics as sm
from sklearn.preprocessing import PolynomialFeatures


# argv是argument variable参数变量的简写形式, sys.argv[1]表示传入的系统命令参数
filename = sys.argv[1]
X = []  # 数据
Y = []  # 标记
with open(filename, 'r') as f:
    for line in f.readlines():  # 解析每行数据，用逗号分割字段
        xt, yt = [float(i) for i in line.split(',')]  # 把字段转化为浮点数，并保存
        X.append(xt)
        Y.append(yt)
'''
为了检查模型是否达到一定的满意度, 把数据分成两组:训练数据集training dataset和测试数据集testing dataset
训练数据集用来建立模型, 测试数据集用来验证模型对未知数据的学习效果
----------
这里把80%的数据作为训练数据集, 20%的数据作为测试数据集
'''
num_training = int(0.8*len(X))
num_test = len(X) - num_training

# 训练数据
X_train = np.array(X[:num_training]).reshape(-1, 1)  # --->此处有问题
Y_train = np.array(Y[:num_training])

# 测试数据
X_test = np.array(X[num_training:]).reshape(-1, 1)  # --->此处有问题
Y_test = np.array(Y[num_training:])

# 创建一个回归器对象
# 创建线性回归对象
linear_regressor = linear_model.LinearRegression()
# 用训练数据集训练模型
linear_regressor.fit(X_train, Y_train)

# 训练数据集图像
y_train_pred = linear_regressor.predict(X_train)  # 对y的预测值
plt.figure()
plt.scatter(X_train, Y_train, color='green')
plt.plot(X_train, y_train_pred, color='black', linewidth=4)
plt.title('Training data')
plt.show()

# 测试数据集图像
y_test_pred = linear_regressor.predict(X_test)

plt.scatter(X_test, Y_test, color='green')
plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.title('Test data')
plt.show()

'''
* 保存数据模型
    保存模型成文件，下次使用时只需加载即可

    1. 在Python文件regressor.py中加入代码
'''
output_model_file = 'saved_model.pkl'  # 保存模型的文件名
with open(output_model_file, 'wb') as f:
    pk.dump(linear_regressor, f)

# 初始化岭回归器
ridge_regressor = linear_model.Ridge(
    alpha=0.01, fit_intercept=True, max_iter=10000)
# 其中alpha参数控制了岭回归器的复杂程度.当alpha趋于0时,岭回归器就是普通最小二乘法的线性回归器
# 如果希望对异常值不那么敏感,就要调大alpha

# 训练岭回归器
ridge_regressor.fit(X_train, Y_train)
y_test_pred_ridge = ridge_regressor.predict(X_test)

print("Mean squared error =", round(
    sm.mean_squared_error(Y_test, y_test_pred), 2))
print("R2 score =", round(sm.r2_score(Y_test, y_test_pred)))

print("Mean squared error =", round(
    sm.mean_squared_error(Y_test, y_test_pred_ridge), 2))
print("R2 score =", round(sm.r2_score(Y_test, y_test_pred_ridge)))

# 多项式回归器
polynomial = PolynomialFeatures(degree=3)  # 多项式次数初始化为3
X_train_transformed = polynomial.fit_transform(
    X_train)  # 表示多项式形式的输入, 与线性回归模型一样大
datapoint = [0.39, 2.78, 7.11]
poly_datapoint = polynomial.fit_transform(datapoint)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(X_train_transformed, Y_train)
print("\nLinear regression:", linear_regressor.predict(datapoint))[0]
print("\nPolynomial regression:", poly_linear_model.predict(poly_datapoint))[0]
