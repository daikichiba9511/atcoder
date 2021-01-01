# https://qiita.com/drken/items/97e37dd6143e33a64c8c
#　めぐる式二分探索

from typing import List, Union
Vector = List[int]

a : Vector = [1, 14, 32, 51, 51, 243, 419, 750, 910]

# index が　条件を満たすかどうか
def isOk(index : int, key : int) -> bool :
    if (a[index] >= key) :
        return True
    else:
        return False

# 汎用的二分探索のテンプレ
def binarySearch(key : int) -> int :
    # 「index = 0」が条件を満たすこともあるので、初期値は−１
    left : int = -1
    right : int = len(a)

    # どんな二分探索でもここの書き方を変えずにできる
    while (right - left > 1) :
        mid : int = left + (right - left) // 2

        if isOk(mid, key) :
            right = mid
        else :
            left = mid
    # left は条件を満たさない最大の値、right は条件を満たす最小の値になっている
    return right

def test() :
    print(binarySearch(51))
    print(binarySearch(1))
    print(binarySearch(910))
    print(binarySearch(52))
    print(binarySearch(52))
    print(binarySearch(0))
    print(binarySearch(911))


if __name__ == "__main__" :
    test()
