def love(u):
    print ('I lova ',u)

def display_message():
    print ('本章学习函数的定义\n\n\n')

display_message()

def favorite_book(title):
    print ('我最喜欢的书是：《'+title+'》\n')

favorite_book("瓦尔登湖")

def make_shirt(chima='L',mark='I love python'):
    print ('你要的T-shirt的尺码为：'+chima+'\n图案为：'+mark)

make_shirt()
make_shirt('M')
make_shirt('S','( ╯□╰ )')


def describe_city(city,state='China'):
    print (city.title()+' is in '+state)

describe_city('xi\'an')
describe_city('旧金山','美国')
describe_city('beijing')