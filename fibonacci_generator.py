#coding:utf-8#
'''
运用生成器运算出雯波那契数列

'''
def fib_yield(n):
    '''定义生成器函数
       输出雯波那契数列
    '''
    a, b = 0,1
    for i in range(n):
        '''将函数制作成生成器
        '''
        yield a
        a, b = b,a+b
        
#调用生成器
flag = True
n = int(input("你要输出几项数列？"))    #获取用户输入
for fib_item in fib_yield(n):
    if flag:
        print(f'由生成器生成的数列为：',end=" ")
        flag = False
    print(fib_item,end=" ")
