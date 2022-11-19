N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (10_001) for _ in range(N + 1)]
dp[0][0] = True
# i番目のカードを選ぶ
for i in range(1, N + 1):
    # S以下の部分和でsにできるか探索
    for s in range(S + 1):
        # s > A_iならA_iを選んでsにできる可能性が有
        if s >= A[i - 1]:
            # i-1番目がちょうどs-A_iになっていれば、A_iを選ぶことでsにできるし、選ばないことでもsにできる
            if dp[i - 1][s] or dp[i - 1][s - A[i - 1]]:
                dp[i][s] = True
            else:
                dp[i][s] = False
        else:
            # もしi-1番目が部分和sになっていれば、i番目を選ばないことでsにできる
            if dp[i - 1][s]:
                dp[i][s] = True
            else:
                dp[i][s] = False

enable = False
for i in range(N + 1):
    if dp[i][S]:
        enable = True
        break

print("Yes" if enable else "No")
