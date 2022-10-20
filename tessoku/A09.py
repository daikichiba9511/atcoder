# 累積和を取る範囲に気をつける[1, H+1/W+1)
# 0のときは-1で配列の最後にアクセスしてしまうから
H, W, N = map(int, input().split())

# (x, y) = (B_i, A_i), (D_i, C_i)
grid = [[0] * (W + 2) for _ in range(H + 2)]
for _ in range(N):
    A_i, B_i, C_i, D_i = map(int, input().split())
    grid[A_i][B_i] += 1
    grid[A_i][D_i + 1] -= 1
    grid[C_i + 1][B_i] -= 1
    grid[C_i + 1][D_i + 1] += 1

cumsum = [[0] * (W + 2) for _ in range(H + 2)]
# 横方向の累積和をとる
for i in range(1, H + 2):
    for j in range(1, W + 2):
        cumsum[i][j] = cumsum[i][j - 1] + grid[i][j]

# 縦方向の累積和をとる
for i in range(1, H + 2):
    for j in range(1, W + 2):
        cumsum[i][j] += cumsum[i - 1][j]

# 答えを求める
for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(cumsum[i][j], end=" ")
    print()
