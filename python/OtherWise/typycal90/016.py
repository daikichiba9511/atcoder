N = int(input())
A, B, C = map(int, input().split())
ans = 1 << 63
for x in range(10_000):
    for y in range(10_000 - x):
        z1 = N - A * x - B * y
        z = z1 // C
        if z1 % C != 0 or z1 < 0 or z > 9999:
            continue
        ans = min(ans, x + y + z)
print(ans)
