from __future__ import annotations
import bisect

N, X = map(int, input().split())
A = [int(i) for i in input().split()]

def solve():
    def binary_search(x: int, a: list[int]) -> int:
        """ 二分探索
        """
        left = 0
        right = len(a)
        while left <= right:
            mid = (right + left) // 2
            if x < a[mid]:
                right = mid - 1
            elif x == a[mid]:
                return mid
            else:
                left = mid + 1
        return -1

    A.sort()
    print(binary_search(x=X, a=A) + 1)


A.sort()
print(bisect.bisect_left(A, X) + 1)
