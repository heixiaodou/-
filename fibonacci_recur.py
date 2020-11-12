#coding:utf-8#
'''
运用递归法运算出雯波那契数列

'''

fib_seq = []
n = int(input("你要输出几项数列？") )   #获取用户输入
for i in range(n+1):
    def fib_recur(i):
        """ 递归函数
    输出雯波那契数列"""
        if i <= 1:
            return i
        else:
            return(fib_recur(i-1)+fib_recur(i-2))
    fib_seq.append(fib_recur(i))
print(f'雯波那契数列的前{n}项为:{fib_seq}',end=" ")
