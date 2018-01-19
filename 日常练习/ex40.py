# _*_ coding:UTF-8 _*_

class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

geci = Song(['我是一棵冬天树',
    '我在想你',
    '把对你的思念开成了花朵'])
geci.sing_me_a_song()

foshuo = ['事件诸法','没有善恶','只有刻苦']
foshuo = Song(foshuo)
foshuo.sing_me_a_song()