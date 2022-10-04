import bisect

# 全体ではO((Q+N)logN)

# A_i (1 <= i <= N)
# B_j (1 <= j <= Q)
# j = 1, 2, 3, ..., Qそれぞれについて番号jの生徒の不満度として考えられる最小値
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]


# O(NlogN)
A.sort()

# O((Qlog N)
for b_i in B:
    i = bisect.bisect_left(A, b_i)
    if i == 0:
        a1 = abs(A[0] - b_i)
        print(a1)
        continue

    if i >= N:
        a2 = abs(A[N - 1] - b_i)
        print(a2)
        continue

    a1 = abs(A[i] - b_i)
    a2 = abs(A[i - 1] - b_i)
    ans = min(a1, a2)
    print(ans)
