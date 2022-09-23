"""
numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。

numpy.fromiter(iterable, dtype, count=-1)
iterable	可迭代对象
dtype	返回数组的数据类型
count	读取的数据数量，默认为-1，读取所有数据

"""
import numpy as np

# 使用range函数创建列表对象
list = range(5)
it = iter(list)

# 使用迭代器创建ndarray
x = np.fromiter(it, dtype=int)
print(x)
