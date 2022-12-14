# numpy.empty
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
# numpy.empty(shape, dtype = float, order = 'C')
# order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
import numpy as np
x=np.empty([3,2],dtype=int)
print(x)

# 注意 − 数组元素为随机值，因为它们未初始化。