'''
使用误差来评价回归器的拟合效果
误差=|实际值-预测值|
-------------
    回归器的拟合效果可以用以下这几个指标metric去衡量:
* 平均绝对误差
    给定数据集中的所有数据点的绝对误差平均值
* 均方误差
    给定数据集的所有数据点的误差的平方的平均值
* 中位数绝对误差
    给定数据集的所有数据点的误差的中位数。这个指标的主要优点是可以消除异常值的干扰。
    # todo 测试数据集中的单个坏点不会影响整个误差指标,均值误差指标会受到异常点的影响
* 解释方差分
    这个分数用于衡量模型对于数据集波动的解释能力。最好的得分是1.0
* R方得分
    指确定相关系数，用于衡量模型对未知样本预测的结果.最好的得分是1.0
--------------
scikit-learn模块调用
'''
import sklearn.metrics as sm

from 机器学习.监督学习.regressor import X_test, Y_test, y_test_pred,output_model_file,pk

print("MAE", round(sm.mean_absolute_error(Y_test, y_test_pred))) # 第一个参数为实际值，第二个参数为预测值
print("MSE", round(sm.mean_squared_error(Y_test, y_test_pred))) # 略
'''
* 保存数据模型
    保存模型成文件，下次使用时只需加载即可
    1. 在Python文件regressor.py中加入代码
    
    import cPickle as pickle

    output_model_file = 'saved_model.pkl' # 保存模型的文件名
    with open(output_model_file, 'w') as f:
        pickle.dump(linear_regressor, f)
    
'''
# 加载并使用模型文件
with open(output_model_file, 'rb') as f:
    model_linregr = pk.load(f)

y_test_pred_new = model_linregr.predict(X_test)
print("\nNew mean absolute error =", round(sm.mean_absolute_error(Y_test, y_test_pred_new), 2))