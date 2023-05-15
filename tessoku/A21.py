import numpy as np

N = int(input())
P = np.zeros(N + 2, dtype="i4")
A = np.zeros(N + 2, dtype="i4")
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

print(P)
print(A)

dp = np.zeros((N + 2, N + 2), dtype="i4")
dp[1][N] = 0
for length in range(N - 2, -1, -1):
    for l in range(1, N - length + 1):
        r = l + length
        print(f"{length=}: ({l=},{r=})")

        # score1の値(l-1番目のブロックを取り除く時の得点)を求める
        score1 = 0
        if l <= P[l - 1] <= r:
            score1 = A[l - 1]

        # score2の値(r+1番目のブロックを取り除く時の得点)を求める
        score2 = 0
        if l <= P[r + 1] <= 1:
            score2 = A[r + 1]

        # dp[l][r] を求める
        if l == 1:
            dp[l][r] = dp[l][r + 1] + score2
        elif r == N:
            dp[l][r] = dp[l - 1][r] + score1
        else:
            dp[l][r] = max(dp[l - 1][r] + score1, dp[l][r + 1] + score2)

print(f"{dp}")
ans = 0
for i in range(1, N + 1):
    if dp[i][i] > ans:
        ans = dp[i][i]
print(f"{ans=}")
