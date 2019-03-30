import time

start_time = time.time()

answer = 2
fib_pos = 1000
a = 1
b = 1

while True:
    if len(str(b)) == fib_pos:
        break
    a, b = b, a + b
    answer += 1

print("Answer:", answer)
print("Time  :", time.time() - start_time)
