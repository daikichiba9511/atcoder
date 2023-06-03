N, A, B = map(int, input().split())

dp = [False] * (N + 1)
for i in range(N):
    if i >= A and not dp[i - A]:
        dp[i] = True
    elif i >= B and not dp[i - B]:
        dp[i] = True
    else:
        dp[i] = False

if dp[N - 1]:
    print("First")
else:
    print("Second")
