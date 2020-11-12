#coding:utf-8#
'''
运用矩阵计算出雯波那契数列

'''
import numpy as np    #调用numpy库实现对矩阵的运算
fib_mat = np.array([[1,0]])
fun_mat = np.array([[1,1],[1,0]])
n = int(input("你要输出几项数列？"))    #获取用户输入
for i in range(n):
    if i == 0:
        print(fib_mat[0][1],end=" ")
    else:
        fib_mat = fib_mat.dot(fun_mat ** n)
        print(fib_mat[0][1],end=" ")
