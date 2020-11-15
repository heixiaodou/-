from scipy.stats import binom    #所有统计函数都被放在scipy.stats里
import numpy as np

'''
二项分布
'''
n = 100
p = 0.5
num = np.random.binomial(n,p,size=20)    #生成20个二项分布随机数
median = np.median(num)    #生成中位数
range = np.ptp(num)    #运用np包中的ptp函数求极差
mean,var,skew,kurt = binom.stats(n,p,moments='mvsk')
std = np.std(num, ddof=1)    # ddof表示非自由样本个数（生成标准差）
print("中位数：",median,"极差：",range,"均值：",mean,"方差：",var)
print("标准差：",std,"偏度：",skew,"峰度：",kurt)
