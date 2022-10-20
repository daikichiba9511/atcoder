# 分割して左右から最大値を伝播させるときは必要な固定長の配列を２つ用意
# それぞれに左右から最大値を伝播させて記録する
# クエリに対して答えをもとめる
# indexに注意(いつも間違える、こんがらがる)
# 直感にあうように実装したほうが良い/図を書いて整理する
# 0-originと1-originのずれで間違ってる気がする。問題の制約の範囲に注意する。
# 累積的にmax/minを伝播させることで拡張させれる
N = int(input())
A = [int(i) for i in input().split()]
D = int(input())

# 左から右に最大値を伝播させる
# i = 0のときはP[-1] = 0
P = [0] * N
for i in range(len(A)):
    P[i] = max(P[i - 1], A[i])

# 右から左に最大値を伝播させる
Q = [0] * N
Q[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    Q[i] = max(Q[i + 1], A[i])

# 答えを求める
for _ in range(D):
    L_i, R_i = map(int, input().split())
    L_i -= 1
    R_i -= 1
    print(max(P[L_i - 1], Q[R_i + 1]))
