def power(a, b, m):
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


def division(a, b, m):
    """a * b^(m-2) (mod m) = 1 (mod m)"""
    return (a * power(b, m - 2, m)) % m


M = 10**9 + 7
n, r = map(int, input().split())

# 分子の余りaを計算
# O(n)
a = 1
for i in range(1, n + 1):
    a = a * i % M

# 分母の余りbを計算
b = 1
for i in range(1, r + 1):
    b = b * i % M
for i in range(1, n - r + 1):
    b = b * i % M

# 答えを計算
print(division(a, b, M))
