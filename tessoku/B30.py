H, W = map(int, input().split())


def modpower(a, b, m):
    """繰り返し二乗法 a**b (mod m)
    O(log m)
    """
    p = a
    ans = 1
    # bが2^30以下の場合
    for i in range(30):
        wari = 1 << i  # 2**i
        if b & wari:
            ans = ans * p % m  # aの2**i乗をかける
        p = p * p % m
    return ans


def moddiv(a, b, m):
    return a * modpower(b, m - 2, m) % m


# 分子の余りaを計算
# O(n)
a = 1
for i in range(1, H + W - 1):
    a = a * i % 1000000007

# 分母の余りbを計算
b = 1
for i in range(1, H):
    b = b * i % 1000000007

for i in range(1, W):
    b = b * i % 1000000007

# 答えを計算
print(moddiv(a, b, 1000000007))
