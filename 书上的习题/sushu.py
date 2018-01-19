def jishu():
    n=1
    while True:
        n+=2
        yield n
def guolv(n):
	return lambda x:x%n>0
def sushu():
	yield 2
	it=jishu()
	while True:
		n=next(it)
		yield n
		it=filter(guolv(n),it)
for n in sushu():
	print(n)
	if n>10000:
		break
        
