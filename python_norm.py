import numpy.matlib
from scipy.stats import norm
import numpy as np
'''
正态分布
'''
loc = 5
scale = 10
c = numpy.random.randn(5,10,20)    #生成20个均值为5，标准差为10的正态分布随机数
median = np.median(c)    #生成中位数
range = np.ptp(c)    #运用np包中的ptp函数求极差
mean,var,skew,kurt = norm.stats(loc,scale,moments='mvsk')     #平均值, 方差, 偏度, 峰度
std = np.std(c, ddof=1)    # ddof表示非自由样本个数（生成标准差）

print("中位数：",median,"极差：",range,"均值：",mean,"方差：",var)
print("标准差：",std,"偏度：",skew,"峰度：",kurt)
