"""
numpy.arange
numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：

numpy.arange(start, stop, step, dtype)
start	起始值，默认为0
stop	终止值（不包含）
step	步长，默认为1
dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
"""

# 生成0到5的数组
import numpy as np
x=np.arange(5,dtype=float)
print(x)

# 设置了起始值、终止值及步长：
x=np.arange(10,20,2)
print(x)