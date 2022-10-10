# 标记编码就是要把单词标记转换成数值形式，让算法懂得如何操作标记
from cProfile import label
from sklearn import preprocessing

# 定义一个标记编码器label encoder
label_encoder = preprocessing.LabelEncoder()

# label_encoder对象知道如何理解单词标记，创建一些标记
input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']

# 为这些标记编码
label_encoder.fit(input_classes)
print("\nClass mapping:")
for i, item in enumerate(label_encoder.classes_):
    print(item, "-->", i)

# 也可以通过数字反转回单词
encoded_labels = [2, 1, 0, 3, 1]
decoded_labels = label_encoder.inverse_transform(encoded_labels)  # 解码
print("\nEncoded labels =\n", encoded_labels)
print("Decoded labels =\n", list(decoded_labels))
