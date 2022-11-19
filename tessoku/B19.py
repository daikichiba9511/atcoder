N, W = map(int, input().split())

w, v = [], []
for _ in range(N):
    w_i, v_i = map(int, input().split())
    w.append(w_i)
    v.append(v_i)

dp = [[] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W):
        if j >= w[i]:
            pass
