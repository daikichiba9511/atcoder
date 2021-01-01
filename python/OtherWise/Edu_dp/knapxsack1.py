# maximize the value

def main():
    N, W = map(int, input().split())
    w_s = []; v_s = []

    for _ in range(N):
        w_i, v_i = map(int, input().split())
        w_s.append(w_i); v_s.append(v_i)
    # initilize
    dp = [[0]*(W+1) for _ in range(N+1)]

    # dp loop
    for i in range(N):
        for sum_w in range(W+1):
            # select i th
            if sum_w - w_s[i] >= 0:
                if dp[i + 1][sum_w] < dp[i][sum_w - w_s[i]] + v_s[i]:
                    dp[i + 1][sum_w] = dp[i][sum_w - w_s[i]] + v_s[i]
            # not select i th
            if dp[i + 1][sum_w] < dp[i][sum_w]:
                dp[i + 1][sum_w] = dp[i][sum_w]
    print(dp[N][W])


if __name__ == "__main__":
    main()