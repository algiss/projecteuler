import time
from math import factorial

start_time = time.time()

fakt = map(int, str(factorial(100)))

answ = sum(fakt)

print("Answ:", answ)
print("Time:", time.time() - start_time)
