def main():
    N, W = map(int, input.split())
    weight = []
    value = []
    for _ in range(N):
        w_i, v_i = map(int, input().split())
        weight.append(w_i)
        value.append(v_i)

    # initialize dp table
    dp = [[0] * (W + 1) for _ in range(N)]

    for i in range(N):
        for w in range(W + 1):
            # case: select ith object
            if w - weight[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i]
                                   [w - weight[i]] + value[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

    print(dp[N][W])


if __name__ == "__main__":
    main()
