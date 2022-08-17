n, k = input().split()
k = int(k)

res = [int(c) for c in n[::-1]]
for _ in range(k):
    dec = sum(a * 8 ** i for i, a in enumerate(res))
    res = []
    if not dec:
        res.append(0)
        continue

    while dec:
        dec, r = divmod(dec, 9)
        if r == 8:
            r = 5
        res.append(r)

print(*res[::-1], sep="")
