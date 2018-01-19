def fibonacci(n):
    term = [0,1]
    i = 2
    while i<=n:
        term.append((term[i-1]+term[i-2]))
        i = i+1
    return term[n]


ww = fibonacci(1000)/fibonacci(1001)

print (ww)
