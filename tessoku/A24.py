# LIS
#  1 <= N <= 10^5
#  1 <= A[i] <= 5 * 10^5
import bisect

N = int(input())
A = list(map(int, input().split()))

INF = 10**9 + 1


def solve(N, A):
    # dp[i]: 最後の要素がA[i]であるような部分列のうち、最長のものの長さ
    # 計算量はO(N^2)＝10^10>10^8なのでTLE
    dp = [INF] * (N + 1)
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            # 部分列の条件を満たすか
            # 満たす時、A[j]の後にA[i]を追加したときに長さが増えるか
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[N - 1]


def solve2(N, A):
    # dp[i]: A[i]を最後の要素とするような部分列のうち、最長のものの長さ
    # dp[i]はA[i]より小さいA[j]の中で、dp[j]が最大のものに1を足したもの
    # 計算量はO(NlogN)＝10^7<10^8なのでAC
    dp = [INF] * (N + 1)
    for i in range(N):
        # dp[i]にA[i]を入れる
        # dp[i]より大きいdp[j]のうち、最小のものをdp[i]にする
        # これにより、dp[i]を最後の要素とするような部分列のうち、最長のものの長さを求めることができる
        # 例えば、dp[4]=4, dp[5]=5, dp[6]=6となっているとき、
        # A[7]=4をdp[7]に入れると、dp[7]=5となり、
        # A[7]を最後の要素とするような部分列のうち、最長のものの長さが求められる
        dp[i] = 1


print(solve(N, A))
