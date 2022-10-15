D = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    L_i, R_i = map(int, input().split())
    L.append(L_i)
    R.append(R_i)

# 範囲の入口と出口を記録
# R_i <= Dなので0の分右に一個ずれることも考慮するとD+2まで取る必要が有る
cumsum = [0] * (D + 2)
for i in range(N):
    L_i, R_i = L[i], R[i]
    cumsum[L_i] += 1
    cumsum[R_i + 1] -= 1

# シミュレーション
for i in range(1, D + 1):
    cumsum[i] += cumsum[i - 1]

for i in range(1, D + 1):
    print(cumsum[i])
