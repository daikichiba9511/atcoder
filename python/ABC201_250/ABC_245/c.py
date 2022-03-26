N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False] * 2 for _ in range(N + 1)]

dp[0][0] = True
dp[0][1] = True

for i in range(1, N):
    a = A[i]
    b = B[i]

    if dp[i - 1][0]:
        if abs(A[i - 1] - A[i]) <= K:
            dp[i][0] = True

        if abs(A[i - 1] - B[i]) <= K:
            dp[i][1] = True

    if dp[i - 1][1]:
        if abs(B[i - 1] - A[i]) <= K:
            dp[i][0] = True

        if abs(B[i - 1] - B[i]) <= K:
            dp[i][1] = True

# print(dp)

if dp[N - 1][0] or dp[N - 1][1]:
    print("Yes")
else:
    print("No")
