import time

start_time = time.time()

answer = 0
count = 0
fib_pos = 3


def make_fib(a=1,b=2):
    global answer, count, fib_pos
    if answer:
        return
    if  len(str(b))== fib_pos:
        answer= count
        return
    c=a+b
    count+=1
    make_fib(b,c))


make_fib()

print("Answer:", answer)
print("Time  :", time.time() - start_time)
