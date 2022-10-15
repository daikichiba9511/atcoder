N = input()

digits = len(N) - 1
ans = 0
for n in N:
    ans += int(n) * 2 ** digits
    digits -= 1
print(ans)
