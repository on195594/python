#!/usr/bin/env python3
# -*- coding: utf-8 -*-

h=input("请输入你的身高(m):")
height=float(h)
w=input("请输入你的体重(kg)：")
weight=float(w)
bmi=weight/(height*height)
if bmi<18.5:
	print("你的BMI为:%.1f,过轻" %bmi )
elif 18.5<=bmi<25:
	print("你的BMI为:%.1f,正常" %bmi)
elif 25<=bmi<28:
	print("你的BMI为:%.1f,过重" %bmi)
elif 28<=bmi<32:
	print("你的BMI为:%.1f,肥胖" %bmi)
else:
	print("你的BMI为:%.1f,严重肥胖" %bmi)

