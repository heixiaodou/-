
#coding:utf-8#
'''
运用循环语句运算出雯波那契数列

'''
List = []    #定义初始列表
n = int(input("你要输出几项数列？") )   #获取用户输入
for i in range(n+1):
    if i == 0:
        List.append(0)
    elif i ==1 or i == 2:    #定义数列前两项
        List.append(1)
    else:
        List.append(List[i-1]+List[i-2])    #在初始列表后面添加
print(f'雯波那契数列的前{n}项为:{List}',end=" ")
