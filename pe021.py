import time

start_time = time.time()


def d(n: int) -> int:
    sum_d = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_d += i
    return sum_d


answer = 0
for a in range(1, 10001):
    b = d(a)
    if a == d(b) and a != b:
        answer += b

print("Answer:", answer)
print("Time  :", time.time() - start_time)
