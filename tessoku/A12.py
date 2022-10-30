from __future__ import annotations

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

def check(x: int, target: int, a: list[int]) -> bool:
    """ targetはx秒後の合計枚数s以下か
    """
    s = 0
    # a_i: 何秒ごとに1枚印刷するか (sec/枚)
    # x秒までにa_iは何枚印刷してるかを求めてる
    # 求めた合計の枚数がtarget以上かどうかを判定して返す
    # x秒後にtarget枚数分印刷できるか
    # targetがKに相当して、target以下ならそもそも印刷できないからx秒後では無理
    for a_i in a:
        s += x // a_i
    return s >= target

def binary_search(target: int, a: list[int]) -> int:
    left = 0
    right = 10 ** 9
    while left < right:
        # left + (right - left) / 2
        mid = (left + right) // 2
        # 答えはx秒以下か？
        # Trueなら中央寄りも左にあるってことだから右端の範囲を狭める
        # 反対に、Falseなら中央よりも右側にあるってことだから左端の範囲を狭める
        if check(x=mid, target=target, a=a):
            right = mid
        else:
            left = mid + 1
    return left


print(binary_search(target=K, a=A))
