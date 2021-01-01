from typing import Iterable

def main()->None:
    N:int = int(input()) # お金の総枚数
    Y:int = int(input()) # 答え＝合計金額

    res10000:int = -1
    res5000:int = -1
    res1000:int = -1

    range_N:Iterable[int] = range(N)

    for a:int in range_N: # 10000円の枚数を０〜Nで調べる
        for b:int in range_N: # 5000円の枚数を0~N で調べる
            c:int = N - a - b # 1000円の枚数はN, a, bから決まる
            total:int = 10000*a + 5000*b + 1000*c
            if total == Y:
                res10000 = a
                res5000 = b
                res1000 = c

    print(res10000," ", res5000, " ", res1000)