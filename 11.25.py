from random import*
t=randint(0,100)
x=int()
input('请输入一个数x:')
while True:
    if x==t:
        print('你猜中了')
    elif x>t:
        print('遗憾，太大了')
        break
    else:
        print('遗憾，太小了')
        break
