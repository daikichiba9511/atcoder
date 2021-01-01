# 二分探索

二分探索の初期値の一方がが真、もう一方が偽になるようにして真偽の境目を一つ求める。

```python

from typing import List

import numpy as np

# indexが条件を満たすかどうか
def isOK(index : int, key : int, a : List[int])->bool:
    if a[index] >= key:
        return True
    else:
        return False

# 汎用的な二分探索のテンプレ」
def binary_search(key, a: List[int])->int:
    ng : int = -1
    ok : int = len(a)

    # ok と　ngのどちらが大きいか分からないことを考慮
    while np.abs(ok - ng) > 1:
        mid = int((ok + ng) / 2)
        if isOK(mid, key, a):
            ok = mid
        else:
            ng = mid
    return ok

def main():
    a = [1, 2, 3, 4, 5]
    print(binary_search(50))
```
