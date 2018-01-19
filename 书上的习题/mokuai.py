def _private_1(name):
	return('Hello,%s' % name)
	
def _private_2(name):
	return('Hello,%s' %name)
	
def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

a = greeting('lin')
b = greeting('world')
print(a)
print(b)
