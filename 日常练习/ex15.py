from sys import argv #导入变量

script,filename = argv #script = argv[0]，filename = argv[1]
txt = open(filename) #打开文件，并把打开的文件对象存储在变量中

print ("Here's your file %r:" % filename) #打印一条关于文件名的消息
print (txt.read()) #打印文件的全部内容

print ('Type the filename again:') #提示消息
file_again = input('>') #用户输入文件名称

txt_again = open(file_again) #再次打开文件

print (txt_again.read()) #打印文件内容