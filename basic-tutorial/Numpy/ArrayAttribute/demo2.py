# ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a.shape) #(2,3)

#调整数组大小
b=a.reshape(3,2)
c=a
c.shape=(3,2)
print(b)
print()
print(c)