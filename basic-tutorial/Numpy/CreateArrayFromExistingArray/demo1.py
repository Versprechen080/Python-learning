"""
numpy.asarray
numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个。

numpy.asarray(a, dtype = None, order = None)
a	任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
dtype	数据类型，可选
order	可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
"""

# 将列表转换为ndarray
import numpy as np

x = [1, 2, 3]
a = np.asarray(x)
print(a)

# 将元组转换为ndarray
x = (1, 2, 3)
a = np.asarray(x)
print(a)


"""
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)
"""

# 设置dtype参数
x=[1,2,3]
a=np.asarray(x,dtype=float)
print(a)