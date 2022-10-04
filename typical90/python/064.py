import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumulative_sum = [0]
for a in range(A):
    cumulative_sum.append(cumulative_sum[-1] + a)

for _ in range(Q):
    L, R, V = map(int, input().split())
