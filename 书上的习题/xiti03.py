# _*_ coding:UTF-8 _*_

#电影票程序
active = True
while active:
    age = input('请问你的年龄是多少？输入0退出\n>')

    age = int(age)
    if age == 0:
        active = False
    elif age < 3:
        print ('你不需要买票\n\n\n')
    elif age > 12:
        print ('你需要买15美元一张的票\n\n\n')
    else:
        print ('你需要买10美元一张的票\n\n\n')



