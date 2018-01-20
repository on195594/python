#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numbs = range(1,100)
for numb in numbs:
	if numb == 1:
		print(str(numb)+'st')
	elif numb == 2:
		print(str(numb)+'nd')
	elif numb == 3:
		print(str(numb)+'rd')
	else:
		print(str(numb)+'th')