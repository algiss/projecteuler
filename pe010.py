import time
start_time=time.time()

n=2000000
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1

prim_sum=0
for i in lst:
    prim_sum+=i
print(prim_sum)

print("Time:",time.time()-start_time)
