def make_car(maker,xinghao,**car_info):
    car={}
    car['MK']=maker
    car['DX']=xinghao
    for key,value in car_info.items():
        car[key]=value
    return car

car = make_car('subarlu','outback',color='blue',tow_package=True,jizuo='7')
print (car)
