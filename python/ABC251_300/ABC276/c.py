# -- upsolve

N = int(input())
P = list(map(int, input().split()))

# 後ろから見ていって、P_n-1 > P_n < P_n+1となるnを探す(ここではj)
j = N - 2
while P[j] < P[j + 1]:
    j -= 1

# P_n < P_kを満たす最小のkを探す
k = N - 1
while P[j] < P[k]:
    k -= 1

# 入れ替える
P[j], P[k] = P[k], P[j]
# 性質を満たすnまで表示+残りは降順で表示
print(*P[: j + 1], *P[:j:-1])
