import bisect

N = int(input())
A = list(map(int, input().split()))

B = list(set(A))
B.sort()

for a in A:
    i = bisect.bisect_left(B, a)
    print(i + 1, end=" ")
print()
