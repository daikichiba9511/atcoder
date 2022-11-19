from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

opes_1_memo = -1
opes_2_memo = defaultdict(lambda: 0)

for _ in range(Q):
    q = input()
    i = int(q[0])
    if i == 1:
        _, x_q = map(int, q.split())
        opes_1_memo = x_q
        opes_2_memo = defaultdict(lambda: 0)

    if i == 2:
        _, i_q, x_q = map(int, q.split())
        opes_2_memo[i_q - 1] += x_q

    if i == 3:
        _, i_q = map(int, q.split())
        if opes_1_memo == -1:
            print(A[i_q - 1] + opes_2_memo[i_q - 1])
        else:
            print(opes_1_memo + opes_2_memo.get(i_q - 1, 0))
