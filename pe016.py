import time
start_time=time.time()

n=1000
answ=0

string_num=str(2**n)
for i in string_num:
    answ+=int(i)

print("Answ:",answ)
print("Time:",time.time()-start_time)
