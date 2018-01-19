lista = [1,1,1,1,3,3,3,3,2,2,2,3,4,4,4,3,2,4,1,1,4,8]
listb = set(lista)
listc = {}
for i in listb:
    if lista.count(i)>0:
        listc[i]=lista.count(i)
print (listc)

if __name__ == '__main__':
    pass

