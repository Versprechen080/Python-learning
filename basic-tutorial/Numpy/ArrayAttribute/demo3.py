# ndarray.itemsize 以字节的形式返回数组中每一个元素的大小
import numpy as np
#数组的dtype为int8（1个字节）
x=np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize) # 8/8

y=np.array([1,2,3,4,5],dtype=np.int16)
print(y.itemsize) # 16/8

z=np.array([1,2,3,4,5],dtype=np.float64)
print(z.itemsize) # 64/8
