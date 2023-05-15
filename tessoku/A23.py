N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

# dp[i][S] := i番目までの中から何枚かを選んで、無料で買える品物の集合がSになるようにするときの最小コスト
# 0 <= i <= M
# 0 <= S <= 2**N - 1
# 例：
# i = 3のとき、クーポン3までの中から何枚選べば、品物1,2だけが無料になるか
INF = 10**10
dp = [[INF] * (2**N) for _ in range(M + 1)]

# 0番目のクーポンは何も選ばないという選択肢しかない
# 計算量O(M * 2**N * N) = 10 * 2**10 * 10 = 10 ** 2 * 10 ** 4 = 10 ** 6 <= 10 ** 8
dp[0][0] = 0
for i in range(1, M + 1):
    # べき集合の管理
    for j in range(2**N):
        # already[k] := k番目の品物がすでに選ばれている
        # jのビットを調べる
        already = [False] * N
        for k in range(N):
            if j & (1 << k):
                already[k] = True

        # クーポン券iを選んだ場合の整数表現vを計算する
        # S と T_i の和集合を求める
        v = 0
        for k in range(N):
            if already[k] or A[i - 1][k] == 1:
                v += 1 << k

        # 遷移をする
        # クーポンiを選ばない場合
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # クーポンiを選ぶ場合
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

print(dp[M][(2**N) - 1] if dp[M][(2**N) - 1] != INF else -1)
