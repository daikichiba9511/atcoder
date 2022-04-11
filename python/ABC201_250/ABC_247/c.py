N = int(input())
res = [[] for _ in range(N + 1)]
res[1] = [1]
for n in range(2, N + 1):
    res[n] = res[n - 1] + [n] + res[n - 1]

print(*res[N])
