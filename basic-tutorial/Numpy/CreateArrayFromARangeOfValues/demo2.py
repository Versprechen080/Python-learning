"""
numpy.linspace
numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：

np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

start	序列的起始值
stop	序列的终止值，如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
dtype	ndarray 的数据类型
"""

import numpy as np
a=np.linspace(1,10,10)
print(a)

# 设置元素全部是1的等差数列：
a=np.linspace(1,1,10)
print(a)

# 将 endpoint 设为 false，不包含终止值：
a=np.linspace(10,20,5,endpoint=False)
print(a)

# 以下实例设置间距。
a=np.linspace(1,10,10,retstep=True)
print(a)
b =np.linspace(1,10,10).reshape([10,1])
print(b)