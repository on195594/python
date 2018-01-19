#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operand type(a)')
	if not isinstance(b,(int,float)):
		raise TypeError('bad operand type(b)')
	if not isinstance(c,(int,float)):
		raise TypeError('bad operand type(c)')
	if a==0:
		if b==0:
			if c==0:
				print('x is anything')
			else:
				print('no answer')
		else:
			return print('x=',-(c/b))
	else:
		n=b**2-4*a*c
		if n>=0:
			x1=(-b-math.sqrt(n))/a/2
			x2=(-b+math.sqrt(n))/a/2
			return print('x1=',x1,'\nx2=',x2)
		else:
			return print('no answer')
quadratic(3,8,2)
	
