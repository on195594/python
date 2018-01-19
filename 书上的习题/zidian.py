my_dic = {'one':'1st' , 'two':'2nd' , 'three':'3rd' , 'four':'4th' , 'five':'5th'}
for key,value in my_dic.items():
	print(key + '\n  ' + value)

import re
re_Email1=re.compile(r'^([a-z]+[.]?[a-z]*[@][a-z]+[.][a-z]+)$')
re_Email2=re.compile(r'^([<][A-Z]?[a-z]+[ ][A-Z]?[a-z]+[>][ ][a-z]+[@][a-z]+[.][a-z]+)$')
m=re_Email1.match('someone@gmail.com')
print(m)
n=re_Email1.match('bill.gates@microsoft.com')
print(n)
s=re_Email2.match('<Tom Paris> tom@voyager.org')
print(s)