q = int(input())
N = 300000

X = [-1] * (10_000 + 1)
for i in range(1, q + 1):
    X[i] = int(input())

# エラトステネスの篩
# O(N log log N), ほぼO(N)
deleted = [False] * (N + 1)
for i in range(2, int(N**0.5) + 1):
    if deleted[i]:
        continue
    for j in range(i * 2, N + 1, i):
        deleted[j] = True

for i in range(1, q + 1):
    if deleted[X[i]]:
        print("No")
    else:
        print("Yes")
