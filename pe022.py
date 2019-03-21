import time
import re

start_time = time.time()

abc_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc = {}
for i in range(len(abc_str)):
    abc[abc_str[i]] = i + 1


def d(name: str) -> int:
    sum_d = 0
    for i in name:
        sum_d += abc[i]
    return sum_d


with open("p022_names.txt") as f:
    names = re.findall(r"\w+", str(f.read()))

names.sort()
answer = 0
for i in range(len(names)):
    answer += d(names[i]) * (i + 1)

print("Answer:", answer)
print("Time  :", time.time() - start_time)
