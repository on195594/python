def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print ('You have %d cheeses!' % cheese_count)
    print ('You have %d boxes of crackers!' % boxes_of_crackers )
    print ('Man that\'s enough for a party!')
    print ('Get a blanket.\n')
#定义函数
print ('We can just give the function numbers directly:')
cheese_and_crackers(20,30) #调用函数

amount_of_cheese = 10 #定义变量
amount_of_crackers = 50 #定义变量
cheese_and_crackers(amount_of_cheese,amount_of_crackers) #调用函数

cheese_and_crackers(10+20,6+5) #调用函数
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000) #调用函数
