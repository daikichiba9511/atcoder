from __future__ import annotations


def modpow(a: int, b: int, mod: int) -> int:
    """a^b mod mを二分累乗法で求める"""
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod  # {a^2, a^4, a^8, ...}
        b = b >> 1
    return res


def moddiv(a: int, b: int, mod: int) -> int:
    """a / b のmod mを求める"""
    return (a * modpow(b, mod - 2, mod)) % mod


def init_fact_and_fact_inv(n: int, mod: int) -> tuple[list[int], list[int]]:
    """階乗とその逆元の初期化(Fermatの小定理を利用)"""
    fact = [1] * (n + 1)
    factinv = [0] * (n + 1)
    for i in range(n + 1):
        if i == 0:
            factinv[i] = moddiv(1, fact[i], mod)
            continue
        fact[i] = (i * fact[i - 1]) % mod
        factinv[i] = moddiv(1, fact[i], mod)
    return fact, factinv


def calc_choice_num(fact: list[int], factinv: list[int], mod: int, n: int, r: int) -> int:
    """
    逆元をつかってnCrを高速に計算する
    """
    if n < r or r < 0:
        return 0
    return (fact[n] * factinv[r] % mod) * factinv[n - r] % mod


def query(k: int, n: int, fact: list[int], factinv: list[int], mod: int) -> int:
    """
    Nコ中何個選ぶかを全探索
    そもそもｋが大きいと1コか2コしか選べないのでそこに着目する
    """
    ret = 0
    for a in range(1, (n // k) + 2):
        s1 = n - ((k - 1) * (a - 1))
        ret += calc_choice_num(fact, factinv, mod, s1, a)
        ret %= mod
    return ret


MOD = 1_000_000_007


def main():
    n = int(input())
    fact, factinv = init_fact_and_fact_inv(n, MOD)
    for k in range(1, n + 1):
        ans = query(k, n, fact, factinv, MOD)
        print(ans)


if __name__ == "__main__":
    main()
