from typing import List, Iterable


def main()->None:
    N:int = int(input())
    # 初期状態
    t:List[int] = [0]
    x:List[int] = [0]
    y:List[int] = [0]

    # 入力
    range_N:Iterable[int] = range(N)
    for i in range_N:
        t[i+1], x[i+1], y[i+1] = int(input())

    can:bool = True
    for i in range_N:
        dt:int = t[i+1] - t[i]
        dist:int = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
        if dt < dist:
            can = False
        if dist % 2 != dt % 2: # dist と dt の偶奇は一致
            can = False
    if can:
        print("Yes")
    else:
        print("No")
