from sys import argv
script,filename = argv

#print ('Please type the filename:')
#filename = input('>')
txt = open(filename)
print (txt.read())