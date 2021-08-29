import math

N = int(input())

max_k = math.floor(math.log2(10**18))

res = 0
for k in range(max_k + 1):
    if 2 ** k <= N:
        res = k
    else:
        break

print(res)
