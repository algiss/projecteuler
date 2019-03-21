import time
start_time=time.time()

answ=0

for y in range(1901,2001):
    for m in range(1,13):
        time_str = "01 " + str(m) +" " + str(y)
        timeres = time.strptime(time_str, "%d %m %Y")
        if timeres.tm_wday == 6:
            answ +=1      

print("Answ:",answ)
print("Time:",time.time()-start_time)
