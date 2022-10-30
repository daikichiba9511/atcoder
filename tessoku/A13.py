N, K = map(int, input().split())
A = [int(i) for i in input().split()]

# 愚直に組み合わせ探すとO(N^2)で10^10くらい
# しゃくとり法でO(N)
res = 0
for left in range(N):
    # すくなくても２つ必要
    right = left + 1
    s = 0
    while right < N and A[right] - A[left] <= K:
        s += 1
        right += 1
    res += s
print(res)
