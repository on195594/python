# -*- coding: utf-8 -*-

def triangles(max):
    L=[1]
    n=0
    while n<max:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(0,len(L)-1)]+[1]
        n=n+1
    return 'done'
t=triangles(10)
for i in t:
	print(i)
