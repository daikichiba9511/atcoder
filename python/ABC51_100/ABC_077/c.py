from typing import List

# index が条件をみたかどうか
def isLess(index : int, key : int, a : List[int])->bool:
    if a[index] >= key:
        return True
    else: return False

def isUpper(index : int, key : int, a : List[int])->bool:
    if a[index] > key:
        return True
    else: return False

# 汎用的な二分探索のテンプレ
def binary_search1(key : int, a : List[int])->int:
    left : int = -1 # index = 0 が条件を満たすこともあるので初期値は−１
    right : int = len(a) # index = len(a) -1 が条件満たさないこともある

    # どんな二分探索でもここの書き方を変えずにできる
    while right - left > 1 :
        mid = left + ((right - left + 1) // 2)
        if a[mid] >= key:
            right = mid
        else:
            left = mid
    return right

def binary_search2(key : int, a : List[int])->int:
    left : int = -1 # index = 0 が条件を満たすこともあるので初期値は−１
    right : int = len(a) # index = len(a) -1 が条件満たさないこともある

    # どんな二分探索でもここの書き方を変えずにできる
    while right - left > 1 :
        mid = left + ((right - left + 1) // 2)
        if a[mid] > key:
            right = mid
        else:
            left = mid
    return right

import sys

def main():

    _ = input()
    a_l = sorted(list(map(int, sys.stdin.readline().strip().split())))
    b_l = sorted(list(map(int, sys.stdin.readline().strip().split())))
    c_l = sorted(list(map(int, sys.stdin.readline().strip().split())))

    cnt = 0
    for b in b_l:
        a_under_b_idx : int = binary_search1(b, a_l)
        c_upper_b_idx : int = binary_search2(b, c_l)
        cnt += len(a_l[:a_under_b_idx])*len(c_l[c_upper_b_idx:])
    print(cnt)


if __name__ == '__main__':
    main()

