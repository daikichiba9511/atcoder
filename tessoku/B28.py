N = int(input())


prev = 0
prev2 = 1
res = 0
for i in range(N):
    res = prev + prev2
    res %= 1000000007
    prev2 = prev
    prev = res


print(res)
