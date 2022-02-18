import os
import re
import matplotlib.pyplot as plt
import numpy as np

prefix = os.getcwd()

trainAccPath = os.path.join(
    prefix, 'ExpressionClassification', 'train5000.txt')
fileContent = open(trainAccPath, mode='r').read()
contentArr = fileContent.split('\n')
arr1 = []
arr2 = []
arr3 = []
for index, item in enumerate(contentArr):
    # print(item)
    # print(item.split('\t'))

    pattern = re.compile(r'\s+(\d+\.\d+)\s+.+(\d+\.\d+)')   # 查找数字
    result = pattern.findall(item)  # tuple(1.01,0.45)

    if(len(result)):
        [loss, accuracy] = result[0]
        # print(loss, accuracy)
        arr1.append(index+1)
        arr2.append(float(accuracy))
        arr3.append(float(loss))

plt.plot(arr1, arr2)
# plt.xticks(rotation=90)  # 横坐标每个值旋转90度
# plt.scatter(arr2, arr1)
ax = plt.gca()
plt.xlabel('Time')
plt.ylabel('Accuracy')
np_arr2 = np.array(arr2)
y_max = np.argmax(np_arr2) #最高点索引
plt.annotate(np_arr2[y_max], xy=(y_max, arr2[y_max]), xytext=(y_max, arr2[y_max]))
plt.show()



plt.plot(arr1, arr3)
# plt.xticks(rotation=90)  # 横坐标每个值旋转90度
# plt.scatter(arr2, arr1)
ax = plt.gca()
plt.xlabel('Time')
plt.ylabel('Loss')
np_arr3 = np.array(arr3)
y_min = np.argmin(np_arr3) #最高点索引
print(y_min)
plt.annotate(np_arr3[y_min], xy=(y_min, arr3[y_min]), xytext=(y_min, arr3[y_min]))

plt.show()
