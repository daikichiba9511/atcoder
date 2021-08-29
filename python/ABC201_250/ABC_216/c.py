N = int(input())

ans = ""
while N > 0:
    if N % 2 != 0:
        ans += "A"
        N -= 1
    else:
        ans += "B"
        N = N // 2
print(ans[::-1])