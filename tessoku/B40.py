n = int(input())
a = list(map(int, input().split()))

cnt = {k: 0 for k in range(0, 101)}
for a_i in a:
    mod = a_i % 100
    cnt[mod] += 1

res = 0
for i in range(50):
    j = 100 - i
    if i == 0 or i == 50:
        res += cnt[i] * (cnt[i] - 1) // 2
    else:
        res += cnt[i] * cnt[j]
print(res)

