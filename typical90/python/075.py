from __future__ import annotations

N = int(input())


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def enumerated_divisors(n: int) -> list[int]:
    res = []
    # O(N^{1/2})
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i != 0:
            continue

        res.append(i)
        # 重複してなければ追加
        if n // i != i:
            res.append(n // i)

    # O(nlogn)
    res.sort()
    return res


def factorized_prime(n: int) -> list[tuple[int, int]]:
    res = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i != 0:
            continue

        # 割れる限り割り続ける
        while n % i == 0:
            res.append(i)
            n //= i

    if n != 1:
        res.append(n)
    return res


# print(factorized_prime(1_000_000_000_000))
# => 24


primes = factorized_prime(N)
ans = 0
# 2 ^ 20まで探索
# 2 ^ x >= Kを満たす最小のxを探す
# Kの最大値が2 ^ 20で抑えられるってこと？
# K:=二分木の一番下のノード数
# 探索範囲0~6まででも通る
for x in range(20 + 1):
    if (1 << x) >= len(primes):
        ans = x
        break
print(ans)
