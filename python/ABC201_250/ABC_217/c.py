N = int(input())
p = list(map(int, input().split()))

ans = [""] * N

for i, p_i in enumerate(p):
    ans[p_i - 1] = str(i + 1)

print(" ".join(ans))
