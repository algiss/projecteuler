def f(n):
    if n<=1 :
        return 1
    return n+f(n-1)

for i in range(10):
    print(i,f(i))
