# _*_ coding: UTF-8 _*_

# 询问需要什么车？
que = '请问您需要租社么样的汽车？'
car = input(que)
print ('Let me see if I can find the ',car)

#询问有多少人用餐
s = "请问有多少人用餐？"
c = input(s)
c= int(c)
if c >8:
    print ('不好意思，没有空座了！')
else:
    print ('这边还有几个位置')

#判断10的整数倍
number = input('请输入一个数字：')
number = int(number)

if number % 10 == 0:
    print (number,' 是10的整数倍')
else:
    print (number,' 不是10的整数倍')
