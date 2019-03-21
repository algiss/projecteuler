import time

start_time = time.time()

max_num = 0

for i in range(1000000):
    n = i
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        count += 1
    if max_num < count:
        answ = i
        max_num = count

print("Answ:", answ)

print("Time:", time.time() - start_time)
