import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1_000_000_007


def binpower(a: int, b: int) -> int:
    """べき乗を高速に計算する

    if 奇数: a*x^2
    if 偶数: x^2
    """
    ans = 1
    while b != 0:
        is_odd = b % 2 == 1
        if is_odd:
            ans = ans * a % MOD
        a = a * a % MOD
        b //= 2
    return ans


"""
K * (K - 1) * (K - 2) * (K - 2) * ... * (K - 2)
"""
if K == 1:
    print(1 if N == 1 else 0)

elif N == 1:
    print(K % MOD)

elif N == 2:
    print(K * (K - 1) % MOD)

else:
    # print(K * (K - 1) % MOD * binpower(K - 2, N - 2) % MOD)
    print(K * (K - 1) % MOD * pow(K - 2, N - 2, MOD) % MOD)
