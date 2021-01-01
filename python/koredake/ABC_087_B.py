from typing import Iterable


def main()->None:
    A:int = int(input())
    B:int = int(input())
    C:int = int(input())
    X:int = int(input())
    range_A:Iterable[int] = range(A)
    range_B:Iterable[int] = range(B)
    range_C:Iterable[int] = range(C)

    res:int = 0
    for a in range_A:
        for b in range_B:
            for c in range_C:
                total:int = 500*a + 100*b +50*c
                if total == X: res = total

    print(res)