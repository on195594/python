def liebiao(x,y):
	i = 0
	number =[]

	while i<x:
		number.append(i)
		i += y
	for num in number:
		print (num)
	return number

liebiao(100,3)