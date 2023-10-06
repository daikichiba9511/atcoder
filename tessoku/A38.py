D, N = map(int, input().split())

l, r, h = [], [], []
for _ in range(N):
    x, y, z = map(int, input().split())
    l.append(x)
    r.append(y)
    h.append(z)


limits = [24] * (D + 1)
for i in range(N):
    for j in range(l[i], r[i] + 1):  # L_i<=d<=R_i
        limits[j] = min(limits[j], h[i])

print(sum(limits[1:]))
