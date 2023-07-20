

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

# Grundy数を求める
# grundy[i] : 石がi個のGrundy数
# transit[i] : grundy数がiとなるような遷移ができるか
# 各山の個数のgrundy数を求める
# 後でそれぞれの山のgrundy数のxorをとる
grundy = [0] * (10**6 + 1)
for i in range(10**6 + 1):
    # 遷移できるかどうかを調べる
    transit = [False] * 3
    if i >= x:
        transit[grundy[i - x]] = True
    if i >= y:
        transit[grundy[i - y]] = True

    # 遷移できるならgrundy数を求める
    # i = 0: grundy[0] = 0
    if not transit[0]:
        grundy[i] = 0
    elif not transit[1]:
        grundy[i] = 1
    else:
        grundy[i] = 2

xor_sum = 0
for i in range(n):
    xor_sum ^= grundy[a[i]]
if xor_sum != 0:
    print("First")
else:
    print("Second")
