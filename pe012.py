import time
start_time=time.time()

number=1
triang_num=1

while True:
    divisors=0
    number += 1
    triang_num += number
    divisor=1
    stop=int(triang_num**0.5)
    for divisor in range( 1,stop+1 ):
        if triang_num % divisor == 0:
            divisors +=2
    if divisors > 500:
        answ=triang_num
        break
        


print("Answ:",answ)

print("Time:",time.time()-start_time)
