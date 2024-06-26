from collections import defaultdict

s = input()
n = len(s)
ans = 0
cnt = defaultdict(int)
for j in range(n):
    ans += j - cnt[s[j]]
    cnt[s[j]] += 1
if max(cnt.values()) > 1:
    ans += 1
print(ans)
