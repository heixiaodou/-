#--- coding: utf-8 ---#
''' 猜数游戏
    输入一个0-100整数，进行判断'''
import random
rand_num = random.randint(1,100)    #[1,99]
print("请开始猜数游戏！")
count = 0    #用来记录已经猜测的次数
while True:
    guess = input('请输入一个整数：')
    count += 1
    if not guess.isdigit():     #判断这个字符串是否为数值
        print('请输入整数！')
        continue
    elif(int(guess) > rand_num):
        print('数字偏大！')
        continue
    elif(int(guess) < rand_num):
        print('数字偏小！')
        continue
    else:
        print('恭喜你猜对了！你总共猜了'+str(count)+'次')
        break;
