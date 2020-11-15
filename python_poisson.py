import numpy.matlib
from scipy.stats import poisson
import numpy as np
'''
泊松分布
'''
lam=5
d=np.random.poisson(lam,size=20)    #生成20个参数为5的泊松分布随机数
median = np.median(d)    #生成中位数
range = np.ptp(d)    #运用np包中的ptp函数求极差
mean,var,skew,kurt = poisson.stats(lam,moments='mvsk')
std = np.std(d, ddof=1)    # ddof表示非自由样本个数（生成标准差）
print("中位数：",median,"极差：",range,"均值：",mean,"方差：",var)
print("标准差：",std,"偏度：",skew,"峰度：",kurt)
