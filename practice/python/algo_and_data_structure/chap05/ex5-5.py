"""N個の整数から重複を許して、O(NW)でWを作れるか(個数制限なし部分和問題)

dp[i][j] := i個の数から重複を許して選んだ時に部分和jと一致するかどうか

dp[i + 1][j] = dp[i][j] or dp[i + 1][j - a[i]]

"""


def main():
    N, W = map(int, input().split())
    a = [int(input()) for _ in range(N)]
    dp = [[False] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N):
        for j in range(W + 1):
            if dp[i][j]:
                dp[i + 1][j] = True

            if j >= a[i] and dp[i + 1][j - a[i]]:
                dp[i + 1][j] = True

    if dp[N][W]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
