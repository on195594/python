# _*_ coding: UTF-8 _*_
dreams = []
active = True

while active:
    dream = input('你梦想的地方是哪里？\n>')

    if dream != 'quit':
        dreams.append(dream)
    else:
        active = False
        
print (dreams)