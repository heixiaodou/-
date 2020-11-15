from scipy.stats import uniform   #所有统计函数都被放在scipy.stats里
import numpy as np
import math
'''
均匀分布
'''
loc = 0.5    #均值
scale = math.sqrt(1/12)    #标准差
a = np.random.uniform(0, 1, 20)   #生成20个0-1均匀分布随机数
median = np.median(a)    #生成中位数
range = np.ptp(a)    #运用np包中的ptp函数求极差
mean,var,skew,kurt = uniform.stats(loc,scale,moments='mvsk')
std = np.std(a, ddof=1)    # ddof表示非自由样本个数（生成标准差）
print("中位数：",median,"极差：",range,"均值：",mean,"方差：",var)
print("标准差：",std,"偏度：",skew,"峰度：",kurt)
