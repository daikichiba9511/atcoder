# Traveling Salesman Problem
# 2 <= N <= 15
# 0 <= X_i <= 1000
# 0 <= Y_i <= 1000

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


def calc_dist(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5


# dp[通った都市の集合][現在いる都市] = 最小コスト
INF = 10**10
dp = [[INF] * N for _ in range(1 << N)]

dp[0][0] = 0
for i in range(2**N):
    for j in range(N):
        if dp[i][j] >= INF:
            continue
        # city i -> city k
        for k in range(N):
            # すでに通った都市は通らない
            # 10進数が偶数の時は、2進数の最下位ビットが0
            # 10進数が奇数の時は、2進数の最下位ビットが1
            # 例えば、i = 3のとき、2進数は11
            # 3 / 2 = 1 ... 1
            # 1 / 2 = 0 ... 1
            # i = 4のとき、2進数は100
            # 4 / 2 = 2 ... 0
            # 2 / 2 = 1 ... 0
            # 1 / 2 = 0 ... 1
            # i = 101のとき、2進数は1100101
            # 101 / 2 = 50 ... 1
            # 50 / 2 = 25 ... 0
            # 25 / 2 = 12 ... 1
            # 12 / 2 = 6 ... 0
            # 6 / 2 = 3 ... 0
            # 3 / 2 = 1 ... 1
            # 1 / 2 = 0 ... 1
            # i = 4 = 100(mod2), k = 2のとき, 4 // 2**2 = 1
            if (i // (2**k)) % 2 == 1:
                continue
            dist = calc_dist(XY[j], XY[k])
            # i + 2**k は、iのk番目のビットを1を立てる
            # i = 3 = 11, k = 3 -> 3 + 2**3 = 3 + 8 = 11 = 1011(mod2)
            dp[i + (2**k)][k] = min(dp[i + (2**k)][k], dp[i][j] + dist)

# 始点に戻る時の総コスト
print(dp[(1 << N) - 1][0])
