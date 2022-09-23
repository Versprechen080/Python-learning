# ndarray.ndim 用于返回数组的维数 等于秩
import numpy as np

a = np.arange(24)  # 数组大小为24 下标0-23
print(a.ndim)  # 1个维度
# 调整大小
b = a.reshape(2, 4, 3)  # 3个维度
print(b.ndim)
