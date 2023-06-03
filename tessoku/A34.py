N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# Grundy数を求める
# 1 <= N <= 10**5
# 1 <= X < Y <= 10**9
# 1 <= A[i] <= 10**9
# 変数 grundy[i]: 石がi個あるときのGrundy数
# 変数 Transit[i]: Grundy数がiとなるような遷移ができるか
# 石が最大で10**5個あるので、grundy数のslotは10**5個用意する
# grundy数は0, 1, 2の3種類
M = 10 ** 5
grundy = [0] * M
for i in range(M):
    transit = [False] * 3

    if i >= X:
        transit[grundy[i - X]] = True
    if i >= Y:
        transit[grundy[i - Y]] = True

    # transit[0] is False
    if not transit[0]:
        grundy[i] = 0
    # transit[1] is False
    elif not transit[1]:
        grundy[i] = 1
    # transit[2] is False
    else:
        grundy[i] = 2

# 出力
xor_sum = 0
for i in range(N):
    xor_sum ^= grundy[A[i]]

if xor_sum != 0:
    print("First")
else:
    print("Second")
