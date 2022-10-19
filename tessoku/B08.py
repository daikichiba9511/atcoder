N = int(input())
X = []
Y = []
for _ in range(N):
    X_i, Y_i = map(int, input().split())
    X.append(X_i)
    Y.append(Y_i)

Q = int(input())

# 各座標に何個の点があるかを二次元配列を使って記録しておく
# O(XY+Q)

grid = [[0] * 1502 for _ in range(1502)]
for y in Y:
    for x in X:
        grid[y][x] += 1

cumsum = [[0] * 1502 for _ in range(1502)]

# 横方向に累積和
for y in range(1, 1502):
    for x in range(1, 1502):
        cumsum[y][x] = cumsum[y][x - 1] + grid[y][x]

# 縦方向に累積和
for y in range(1, 1502):
    for x in range(1, 1502):
        cumsum[y][x] += cumsum[y - 1][x]

# 答えを求める
# a <= x <= c
# b <= y <= d
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(f"{cumsum[b - 1:d][a - 1:c] = }")
    print(cumsum[d][c] - cumsum[d][a - 1] - cumsum[b - 1][c] + cumsum[b - 1][a - 1] )


