from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())

A.sort()
for _ in range(Q):
    X = int(input())
    print(bisect_left(A, X))
