n = int(input())
a = list(map(int, input().split()))

cnt = {}
for i in range(1, 101):
    cnt[i] = a.count(i)

res = 0
for i, c in cnt.items():
    res += c * (c - 1) * (c - 2) // 6
print(res)

