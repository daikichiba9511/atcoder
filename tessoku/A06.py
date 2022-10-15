N, Q = map(int, input().split())
A = [int(i) for i in input().split()]

# 累積和を取る
# 0を用意するのは境界にも正しく答えられるようにするため
# S_0=0があるとS_R - S_{0}ができる
cumsum = [0]
for i in range(len(A)):
    cumsum.append(cumsum[-1] + A[i])

# シミュレーション
for _ in range(Q):
    L, R = map(int, input().split())
    print(cumsum[R] - cumsum[L - 1])
