def main():
    N, W = map(int, input().split())
    a = []
    for _ in range(N):
        a.append(int(input()))

    dp = [[False * (N + 1)] for _ in range(W + 1)]
    dp[0][0] = True
    for i in range(N + 1):
        for j in range(W + 1):
            # case1: a[i] is NOT selected
            if dp[i][j]:
                dp[i + 1][j] = True

            # case2: a[i] is selected
            # J - a[i] >= 0 is need
            if j >= a[i] and dp[i][j - a[i]]:
                dp[i + 1][j] = True

    if dp[N][W]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print("elapsed time : ", time.time() - start)
