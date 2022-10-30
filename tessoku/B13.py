N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和を事前に計算
cumsum = [0]
for i in range(len(A)):
    cumsum.append(cumsum[-1] + A[i])


cnt = 0
left = 1
right = 1
# しゃくとり法+累積和で[l,r)区間和をO(1)でもとめる
# 全体でO(N)
while left <= N:
    if right <= N and cumsum[right] - cumsum[left - 1] <= K:
        cnt += 1
        right += 1
    else:
        left += 1
        right = left
print(cnt)
