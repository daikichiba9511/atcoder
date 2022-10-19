H, W = map(int, input().split())
X = [[0] * (W + 1) for _ in range(H + 1)]
for h in range(1, H + 1):
    X_i = [int(i) for i in input().split()]
    for w in range(1, W + 1):
        X[h][w] = X_i[w - 1]

Q = int(input())


# 累積和の多次元配列の初期化
# cumsum_0,i = 0, cumsum_i,0を入れる必要がある
# 左上の点の左上の点とその点と同じ高さ、同じ幅の部分の点の座標を引くから
# 統一的に扱える
cumsum = [[0] * (W + 1) for _ in range(H + 1)]


# 横方向に累積和をとる
for h in range(1, H + 1):
    for w in range(1, W + 1):
        cumsum[h][w] = cumsum[h][w - 1] + X[h][w]


# 縦方向に累積和をとる
for w in range(1, W + 1):
    for h in range(1, H + 1):
        cumsum[h][w] += cumsum[h - 1][w]


# 答えを求める
for i in range(Q):
    A_i, B_i, C_i, D_i = map(int, input().split())
    ans = cumsum[C_i][D_i] + cumsum[A_i - 1][B_i - 1] - cumsum[A_i - 1][D_i] - cumsum[C_i][B_i - 1]
    print(ans)
