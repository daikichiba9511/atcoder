T = int(input())
N = int(input())

L = []
R = []
for _ in range(N):
    L_i, R_i = map(int, input().split())
    L.append(L_i)
    R.append(R_i)

# 範囲内での人の出入りを記録する
cumsum = [0] * (T + 2)
for i in range(N):
    cumsum[L[i]] += 1
    cumsum[R[i]] -= 1

# 累積和をとる
for i in range(1, T + 1):
    cumsum[i] += cumsum[i - 1]

print(f"{cumsum = }")
for t in range(T):
    print(cumsum[t])
