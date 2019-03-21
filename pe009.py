import time
start_time=time.time()
found = False
for a in range(1,int(1000/2)):
    if found : break
    for b in range(1,int(1000/3)):
        c=1000-a-b
        if  c**2 == a**2+b**2:
            print(a*b*c)
            found=True
            break 
print("Time:",time.time()-start_time)
