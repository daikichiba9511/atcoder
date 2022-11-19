N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


dp = [0] * (N + 1)
dp[0] = 0
dp[1] = dp[0] + A[0]
for x in range(2, N):
    dp[x] = min(dp[x - 1] + A[x - 1], dp[x - 2] + B[x - 2])


ans = []
# 逆順から復元していく
pos = N - 1
while True:
    ans.append(pos + 1)
    if pos == 0:
        break

    if dp[pos - 1] + A[pos - 1] == dp[pos]:
        pos = pos - 1
    else:
        pos = pos - 2

print(len(ans))
print(*ans[::-1])
