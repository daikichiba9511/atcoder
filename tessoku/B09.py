N = int(input())

# (X, Y) = (A_i, B_i), (C_i, D_i)
# 0 <= A_i < C_i <= 1500
# 0 <= B_i < D_i <= 1500
# 要素数は1501
# grid[i][j] := 座標(i+0.5, j+0.5)には何枚の加味が置かれてるか
grid = [[0] * 1503 for _ in range(1503)]
for _ in range(N):
    A_i, B_i, C_i, D_i = map(int, input().split())
    grid[A_i + 1][B_i + 1] += 1
    grid[A_i + 1][D_i + 1] -= 1
    grid[C_i + 1][B_i + 1] -= 1
    grid[C_i + 1][D_i + 1] += 1


# 横方向に累積和
for i in range(1, 1501):
    for j in range(1, 1501):
        grid[i][j] += grid[i][j - 1]

# 縦方向に累積和
for i in range(1, 1501):
    for j in range(1, 1501):
        grid[i][j] += grid[i - 1][j]

# 答えを求める
ans = 0
for i in range(1501):
    for j in range(1501):
        if grid[i][j] >= 1:
            ans += 1
print(ans)
