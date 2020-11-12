#coding:utf-8#
'''
运用迭代器运算出雯波那契数列

'''

fib_seq = []
n = int(input("你要输出几项数列？") )   #获取用户输入
class Fibonacci_class:

    def __init__(self,n):
        self.a = 0    #计算项数
        self.num_1 = 0
        self.num_2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a == 0:
            self.num_1, self.num_2 = self.num_1, self.num_2  
        elif self.a <= n+1:
            self.num_1, self.num_2 = self.num_2, self.num_1+self.num_2
        else:
            raise StopIteration    #若超过目标项数则停止迭代，抛出异常
        self.a += 1
        return self.num_1


Fibonacci = Fibonacci_class(n)
for i in range(n):
    fib_seq.append(next(Fibonacci))    #用next方法将返回结果依次放入列表中
print(f'雯波那契数列的前{n}项为:{fib_seq}',end=" ")

