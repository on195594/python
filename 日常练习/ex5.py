my_name = 'Zed A. Shaw'
my_age = 33 # not a lie
my_height = 74 # inch
my_weight = 130 # lbs
my_eyes = 'blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %e cm tall." % (my_height*2.54))
print ("He's %e kg heavy." % (my_weight*453.59/1000))
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes,my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# This line is tricky,try to get it exactly right
print('If I add %d %d,and %d I get %d.' %(
	my_age,my_height,my_weight,my_age+my_height+my_weight))
