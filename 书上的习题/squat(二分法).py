def squat(x,epsilon):
    high = max(x,1.0)
    low = 0
    crt = 0
    guess = (high+low)/2.0
    while abs(guess**2-x)>epsilon and crt<=100:
        if guess**2>x:
            high = guess
        else:
            low = guess
        guess = (high+low)/2.0
        crt +=1
    print ("循环次数：%r ,%r的平方根是：%r" %(crt,x,guess))
    return guess
squat(7,0.00000000000000001)

