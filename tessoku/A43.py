n, l = map(int, input().split())
ab = [input().split() for _ in range(n)]

ans = 0
for a, b in ab:
    a = int(a)
    if b == "E":
        ans = max(ans, l - a)
    else:
        ans = max(ans, a)
print(ans)
