# _*_ coding: UTF-8 _*_

sandwich_orders = ['回锅肉','青椒炒肉','韭菜鸡蛋','回锅肉','油焖茄子','辣子鸡丁','回锅肉']
finished_sandwich = []

for s in sandwich_orders:
    print ('%s 来啦！' % s)
    finished_sandwich.append(s)

for f in finished_sandwich:
    print (f)

print ('回锅肉卖完了！')

while '回锅肉' in sandwich_orders:
    sandwich_orders.remove('回锅肉')
print (sandwich_orders)