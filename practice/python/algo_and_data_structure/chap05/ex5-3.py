def main():
    N = int(input())
    p = list(map(int, input().split()))
    W = sum(p)

    dp = [[False] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = True

    # dp loop
    res = []
    for i in range(N):
        for j in range(W):
            if dp[i][j]:
                dp[i + 1][j] = True
                res.append(j)

            if j >= p[i] and dp[i][j - p[i]]:
                dp[i + 1][j] = True
                res.append(j)

    print(len(set(res)) + 1)


if __name__ == "__main__":
    main()
