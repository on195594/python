 #!/usr/bin/env python3
 # -*- coding:utf-8 -*-

#列表练习，解决不能用户收到不同的提示
users=['lin','admin','abcd','lisa','wins','girl']
if users:
    for user in users:
	    if user == 'admin':
		    print('Hello '+user+',would you like to see a status report?')
	    else:
		    print('Hello '+user+',thank u for logging in again')
else:
	print('We need some users!')

#列表练习,解决用户名注册问题
current_users = ['lin', 'meimei', 'MengQiong', 'liujiao', 'yuesha']
new_users = ['mengqiong', 'Lin', 'admin', 'waer', 'blue']
for new_user in new_users:
	if new_user.lower() in map(lambda x : x.lower(),current_users):
		print(new_user+'已经被使用，请更换用户名！')
	else:
		print(new_user+'没有被使用')