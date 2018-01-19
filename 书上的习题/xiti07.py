# _*_ coding:UTF-8 _*_
#hanshu1
def city_country(city,country):
    cc = city+','+' '+country
    return cc.title()

print (city_country("xi'an","china"))
print (city_country('shanghai','china'))
print (city_country('taibei','taiwan'))



#hanshu2
def make_album(singer_name,album_name,song_num=None):
    singer_name = singer_name.title()
    album_name = album_name.title()
    if song_num :
        cd = {'singer':singer_name,'album':album_name,'song_nums':song_num}
    else:
        cd = {'singer':singer_name,'album':album_name}
    return cd
# 调用函数
cd1 = make_album('许巍','two days',2)
cd2 = make_album('angle','love',12)
cd3 = make_album('wangfei','星空')

print (cd1)
print (cd2)
print (cd3)
# 循环调用函数
while True:
    singer = input('请输入歌手名字,或者任何时候输入"q"退出\n>')
    if singer == 'q':
        break
    ablum = input ('请输入专辑名称\n>')
    if ablum == 'q':
        break
    cd = make_album(singer,ablum)
    print (cd)
