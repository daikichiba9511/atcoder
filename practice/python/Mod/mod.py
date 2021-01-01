from typing import List

MOD = 1000000007

def mod_try():
    a = 111111111
    b = 123456789
    c = 987654321
    print(a * b * c % MOD)
    print(a * b % MOD * c % MOD)

def mod_try2():
    print(-17 % 5)

# a ^ n mod を計算する
def mod_pow(a, n, mod):
    res = 1
    while (n > 0):
        if n & 1 :
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

# a ^ {-1} mod を計算する
def mod_inv(a, mod):
    return mod_pow(a, mod-2, mod)

def mod_try3():
    # mod. 13 の逆元を求める
    for i in range(1, 13):
        print(i," 's inv : ", mod_inv(i, 13))

# ==============================================================
# 二項係数
from typing import List, Union
Num = Union[int, float]
Vector = List[Num]

MAX : int = 510000
MOD : int = 1000000007

fac : List[int] = [1] * MAX
finv : List[float] = [1.] * MAX
inv : List[float] = [1.] * MAX

# テーブルを作る前処理
def com_init():
    fac[0] = fac[1] = 1
    finv[0] = fac[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

# 二項係数計算
def com(n : int, k : int)->Num:
    if n < k :
        return 0
    if (n < 0) or (k < 0) :
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

def mod_try4():
    # 前処理
    com_init()

    # 計算例
    print(com(100000, 50000))

if __name__ == "__main__":
    mod_try4()