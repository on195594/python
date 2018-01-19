class Restaurant(object):
    """This is restaurant"""
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print (self.restaurant_name.title() + ':' + self.cuisine_type.title())

    def open_restaurant(self):
        print ('This' + self.restaurant_name.title() +'is opening')

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,innumber):
        self.number_served += innumber

kfc = Restaurant('KFC','kuaican')
kfc.describe_restaurant()
kfc.open_restaurant()
huangmengji = Restaurant('黄焖鸡米饭','中餐')
huangmengji.describe_restaurant()

xiaofeiyang = Restaurant('小肥羊','火锅')
xiaofeiyang.describe_restaurant()

restaurant = Restaurant('KFC','kuaican')
print (restaurant.number_served)
restaurant.number_served = 20
print (restaurant.number_served)
restaurant.set_number_served(40)
print (restaurant.number_served) 
restaurant.increment_number_served(120)
print (restaurant.number_served)

class IceCreamStand(Restaurant):
    """docstring for IceCreamStand Restaurant """
    def __init__(self, restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = ['巧克力','香草','芒果','菠萝','milk']

    def IceCream_flavor(self,flavor):
        for f in self.flavor:
            print ('This is the '+ f +' IceCream')

bingqiling = IceCreamStand('遇见','love')
bingqiling.IceCream_flavor(bingqiling.flavor)

