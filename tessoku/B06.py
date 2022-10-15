N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())

# 勝利数の累積和をとる
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1] + a)

for _ in range(Q):
    L, R = map(int, input().split())
    win_num = cumsum[R] - cumsum[L - 1]
    mid = (R - L + 1) / 2
    if win_num > mid:
        print("win")
    elif win_num == mid:
        print("draw")
    else:
        print("lose")
