N = int(input())

def f(x: float) -> float:
    return x ** 3 + x

def bin_search(target: int) -> float:
    left = 0
    right = 10 ** 15 + 10 ** 5

    while right - left > 10e-6:
        mid = (left + right) / 2
        # f(x)は単調増加関数だからtargetよりもちいさかったらxを増やしたい
        # 範囲の左端を狭めればその中点は増える
        if target > f(mid):
            left = mid
        else:
            right = mid
    return left

print(bin_search(target=N))
