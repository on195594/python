# _*_ coding:UTF-8 _*_
#比萨配料

active = True

while active:
    pl = input('请输入一些比萨配料：')
    if pl == 'quit':
        active = False
    else:
        print ('我们将添加%s' %pl)