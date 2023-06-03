N = int(input())
TA = [tuple(input().split()) for _ in range(N)]

# O(N)
# 1 <= N <= 10**5
res = 0
for t, a in TA:
    if t == "+":
        res += int(a)
    elif t == "-":
        res -= int(a)
    else:
        res *= int(a)

    res %= 10000
    print(res)
