
# chmin can't use
# List in Python create copy by using slice

def main():
    INF = 10 ** 9
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    # memo of cost of i th avalable going range
    dp = [INF] * (N + 10)

    # condition of init
    dp[0] = 0

    #
    for i in range(N):
        for k in range(1, K+1):
            if i + k >= len(h):break
            tmp_cost = dp[i]+ abs(h[i] - h[i + k])
            if tmp_cost < dp[i + k]:
                dp[i + k] = tmp_cost
    print(dp[N-1])

if __name__ == "__main__":
    main()