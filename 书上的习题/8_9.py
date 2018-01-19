def show_magicians(magicians):
    for magician in magicians:
        print ('Hello'+','+' '+magician.title()+' !')

# show_magicians(lovers)

def make_great(magicians):
    b=[]
    while magicians:
        a = 'the Great' + ' ' + magicians.pop()
        b.append(a)
    for i in b:
        magicians.append(i)
    return magicians
  
lovers = ['lily','baby','minova','mq']
lo = make_great(lovers[:])
show_magicians(lovers)
show_magicians(lo)