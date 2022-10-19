N = int(input())
X = []
Y = []
# O(XY+Q)
# 各座標に何個の点があるかを二次元配列を使って記録しておく
# for y in Y:
#   for x in X:
#     grid[y][x] += 1
# だと(Y_i, X_i)の関係が崩れる{(1, 3), (2, 4)} -> {(1,2),(1,4),(3,2),(3,4)}になっちゃう
# やるならzipでまとめるべきだった
grid = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
    X_i, Y_i = map(int, input().split())
    grid[Y_i][X_i] += 1

Q = int(input())


cumsum = [[0] * 1501 for _ in range(1501)]

# 横方向に累積和
for y in range(1, 1501):
    for x in range(1, 1501):
        cumsum[y][x] = cumsum[y][x - 1] + grid[y][x]

# 縦方向に累積和
for y in range(1, 1501):
    for x in range(1, 1501):
        cumsum[y][x] += cumsum[y - 1][x]

# 答えを求める
# a <= x <= c
# b <= y <= d
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(cumsum[d][c] - cumsum[d][a - 1] - cumsum[b - 1][c] + cumsum[b - 1][a - 1])
