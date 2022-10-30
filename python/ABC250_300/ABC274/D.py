from collections import deque

N, x, y = map(int, input().split())
A = [int(i) for i in input().split()]

# grid = [[False] * (2 * (10 ** 4)) for _ in range(2 * (10 ** 4))]
#
# que = deque()
# que.append((10 ** 4, 10 ** 4))
# prev_h = 10 ** 4
# prev_w = 10 ** 4 + A[0]
# cnt = 1
# while not que:
#     h, w = que.popleft()
#     if h > 2 * (10 ** 4) or w > 2 * (10 ** 4) or h < 0 or w < 0:
#         continue
#
#     grid[h][w] = True
#
#     if prev_w - w == 0:
#         que.append((h, w + A[cnt]))
#         que.append((h, w - A[cnt]))
#     if prev_h - h == 0:
#         que.append((h + A[cnt], w))
#         que.append((h - A[cnt], w))
#     cnt += 1
#
# if grid[y][x]:
#     print("Yes")
# else:
#     print("No")
M = 10 ** 4
# x, yは独立に解いて良い
# nが奇数ならx軸のdp, 偶数ならy軸のdpで解ける
dp_x = [False] * (2 * M + 1)
dp_y = [False] * (2 * M + 1)
dp_x[A[0]] = True
dp_y[0] = True


for n in range(N):
    next_dp = [False] * (2 * M + 1)
    a = A[n]
    if n % 2 == 0:
        for j in range(-M, M + 1):
            next_dp[j + a] = next_dp[j + a] or dp_y[j]
            next_dp[j] = next_dp[j] or dp_y[j + a]
        next_dp, dp_y = dp_y, next_dp
    else:
        for j in range(-M, M + 1):
            next_dp[j + a] = next_dp[j + a] or dp_x[j]
            next_dp[j] = next_dp[j] or dp_x[j + a]
        next_dp, dp_x = dp_x, next_dp

print("Yes" if dp_y[y] and dp_x[x] else "No")
