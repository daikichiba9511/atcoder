H, W = map(int, input().split())
X = []
for _ in range(H):
    X_i = [int(i) for i in input().split()]
    X.append(X_i)
Q = int(input())

# 事前に各行毎に累積和を求めておく
# x_i := i行目の累積和. x_i,0 = 0
cumsum = []
for x in X:
    cumsum_i = [0]
    for x_i in x:
        cumsum_i.append(cumsum_i[-1] + x_i)
    cumsum.append(cumsum_i)


# query実行
# left-top=(A_i, B_i), right-bottom=(C_i, D_i)
# 各行毎に累積和から指定範囲の総和をO(1)で計算
# その後、行ごとの総和の総和をとる
for _ in range(Q):
    A_i, B_i, C_i, D_i = map(int, input().split())
    ans = 0
    for i in range(B_i - 1, D_i):
        row_sum = cumsum[i][C_i] - cumsum[i][A_i - 1]
        print(f"{row_sum = }")
        ans += row_sum
    print(ans)
