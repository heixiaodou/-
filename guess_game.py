
# --- coding: utf-8 ---
import random
guess = random.randint(1,100)
print('猜数游戏！')
SUM = 0
print("请输入数字1-100")
while True:
	a = input('请输入一个整数：')
	if(a == '退出'):
		exit(0)
	elif(int(a) > guess):
		print('数字偏大！')
		SUM = SUM + 1
	elif(int(a) < guess):
		print('数字偏小！')
		SUM = SUM + 1
	elif(int(a) == guess):
		SUM = SUM + 1
		print('恭喜猜对了！你总共猜了' + str(SUM) + '次')
		break;
