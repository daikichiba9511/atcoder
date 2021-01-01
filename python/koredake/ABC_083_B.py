from typing import Iterable
# 各桁の和を計算する関数
def findSumOfDigits(n:int)->int:
    sum:int = 0
    while n > 0: # nが０になるまで繰り返す。
        sum += n % 10
        n /= 10

    return sum


def main()->None:
    N:int = int(input())
    A:int = int(input())
    B:int = int(input())

    total:int = 0
    range_N:Iterable[int] = range(N)
    for i in range_N:
        sum:int = findSumOfDigits(i) #各桁の和
        if A <= sum <= B :
            total += i

    print(total)
