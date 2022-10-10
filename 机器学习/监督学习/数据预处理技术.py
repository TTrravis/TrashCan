import numpy as np
from sklearn import preprocessing

data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])

# 均值移除
# 为了保证特征值均值为0，即标准化处理->为了消除特征彼此间的偏差
data_std = preprocessing.scale(data)
print("\nMean =", data_std.mean(axis=0)) # 此处axis=0表示纵轴平均，axis=1表示横轴平均
print("Std deviation =", data_std.std(axis=0)) # 此处axis=0表示计算纵轴标准差，axis=1表示计算横轴标准差

# 范围缩放
# 数据点中每个特征的数值范围可能变化非常大，因此需要对数值的范围进行缩放
data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)) # 数据归一化方法->将数据点映射到[0,1]区间，feature_range参数可以选择映射到其他区间
data_scaled = data_scaler.fit_transform(data) # fit_transform是fit和transform的组合，既包括训练又包含转换
print("Min max scaled data =\n", data_scaled)

# 归一化
# 用于需要对特征向量的值进行调整，以保证每个特征向量的值都缩放到相同的数值范围
# 最常用的归一化形式是将特征向量调整为L1范数，使特征向量的数值之和为1
# 此方法经常用于确保数据点没有因为特征的基本性质而产生较大差异，即确保数据处于同一数量级，提高不同特征数据的可比性
data_normalized = preprocessing.normalize(data, norm='l1')
print("\nL1 normalized data =\n", data_normalized)

# 二值化
# 二值化用于将数值特征向量转换为布尔类型向量
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print("\nBinarized data =\n", data_binarized)

# 独热编码
# 如果我们要处理的数据是稀疏地、散乱地分布在空间中，但并不需要存储这些大数值，就用到独热编码
# 可看作是一种收紧特征向量的工具。把特征向量的每个特征值都按照这种方式编码，可以更加有效地表示空间
# 如果处理一个四维空间，当给一个特征向量的第n个特征进行编码时，编码器会遍历每个特征向量的第n个特征，让后进行非重复计数
# 如果非重复计数的值是K，那么九八这个特征转换为只有一个值是1其他值都是0的K维向量。
encoder = preprocessing.OneHotEncoder()
encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]])
encoded_vector = encoder.transform([[2,3,5,3]]).toarray()
print("\nEncoded vector =\n", encoded_vector)