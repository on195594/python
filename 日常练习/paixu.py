def paixu(libiao):
    for i in range(1,len(libiao)):
        value = libiao[i]
        j = i-1
        while j>=0 and value<libiao[j]:
            libiao[j+1] =libiao[j]
            libiao[j] = value             
            j = j-1
    return libiao
a= [7,13,4,20,3,1,5,8,3]
paixu(a)
print (a)