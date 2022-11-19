N, W = map(int, input().split())
w_s = []
v_s = []
for _ in range(N):
    w_i, v_i = map(int, input().split())
    w_s.append(w_i)
    v_s.append(v_i)

# dp[i][j] := 1~iまでの中から重さの合計がjとなるように選ぶことを考える。合計価値として有り得る最大値はいくつか？
dp = [[-(10 ** 6)] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(W + 1):
        if j >= w_s[i - 1]:
            # 品物iを選ぶか(dp[i-1][j - w_s[i - 1]] + v_s[i - 1])
            # 品物iを選ばないか(dp[i - 1][j])
            # i - 1までで重みWを越えないように最大値が決まってる時に、i番目の品物を選ぶ/選ばないで最大値を更新する方法は2通り
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_s[i - 1]] + v_s[i - 1])
        else:
            # j < w_s[i - 1]の時は選べない
            dp[i][j] = dp[i - 1][j]

ans = -1
for j in range(W + 1):
    ans = max(ans, dp[N][j])
print(ans)
