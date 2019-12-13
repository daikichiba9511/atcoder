import numpy as np
from typing import List, Iterable

def main()->None:
    # 解説みた。
    c_1: List[int] = list(map(int, input().split()))
    c_2: List[int] = list(map(int, input().split()))
    c_3: List[int] = list(map(int, input().split()))
    c = np.array([c_1, c_2, c_3],dtype=int)

    a = np.empty(3, dtype=int)
    b = np.empty(3, dtype=int)
    
    a[0] = 0
    range_3: Iterable[int] = range(3)
    for j in range_3:
        b[j] = c_1[j] - a[0]
    for i in range(1, 3):
        a[i] = c[i][0] - b[0]

    # 条件通りかどうか判定するのに探索
    good: bool = True
    for i, a_i in enumerate(a):
        for j, b_j in enumerate(b):
            if a_i + b_j != c[i][j]:
                good = False

    if good: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()