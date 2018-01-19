class Animal(object):
    def __init__(self,name,color):
        self.name=name
        self.color=color
		
    def print_color(self):
        print('%s:%s' %(self.name,self.color))
		
    def get_like(self):
        if self.color=='yellow':
            print('I like %s' %self.name)
        if self.name=='dog':
            print('I like %s' %self.name)		
cat=Animal('huahua','yellow')
cat.name
cat.print_color()
cat.get_like()

duoduo=Animal('dog','black')
duoduo.name
duoduo.print_color()
duoduo.get_like()

duoduo.color='white'
duoduo.print_color()
cat.name='meimei'
cat.print_color()

