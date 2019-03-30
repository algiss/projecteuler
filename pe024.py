import time

start_time = time.time()

answer = 0
count = 0
perm_pos = 1000000


def make_permutations(n, m=-1, prefix=None):
    global answer, count, fib_pos
    prefix = prefix or ""
    m = n if m == -1 else m
    if answer:
        return
    if m == 0:
        count += 1
        if count == perm_pos:
            answer= prefix
        return
    for i in range(n):
        if str(i) in prefix:
            continue
        make_permutations(n,m-1,prefix+str(i))


make_permutations(10)

print("Answer:", answer)
print("Time  :", time.time() - start_time)
