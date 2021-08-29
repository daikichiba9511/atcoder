import math

N, M = map(int, input().split())

A = list(map(int, input().split()))


A = [a for a in A if a % 2 != 0]

res = []

for a in A:
    for k in range(1, M + 1):
        if math.gcd(a, k) == 1:
            print("append", a, k)
            res.append(k)

print(len(res))
for i in res:
    print(i)
