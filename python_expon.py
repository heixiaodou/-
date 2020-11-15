import numpy.matlib
from scipy.stats import expon
import numpy as np
'''
指数分布
'''
lam = 10
loc = 1/lam
scale = 1/lam
e = np.random.exponential(lam,size=20)    # 产生20个满足指数分布的随机数
median = np.median(e)    #生成中位数
range = np.ptp(e)    #运用np包中的ptp函数求极差
mean,var,skew,kurt = expon.stats(loc,scale,moments='mvsk') 
std = np.std(e, ddof=1)    # ddof表示非自由样本个数（生成标准差）
print("中位数：",median,"极差：",range,"均值：",mean,"方差：",var)
print("标准差：",std,"偏度：",skew,"峰度：",kurt)
