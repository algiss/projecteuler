import time
start_time = time.time()


def abundand(n):
    div = [i for i in range(1, n//2+1) if n % i == 0]
    return sum(div) > n

numbers = [i for i in range(28124) if abundand(i)]

s = []
for i in numbers:
    for y in numbers:
        if i+y < 28124:
            s += [i+y]

allnumbers = [i for i in range(1, 28124)]

answer = sum(set(allnumbers)-set(s))

print("Answer:", answer)
print("Time  :", time.time() - start_time)
