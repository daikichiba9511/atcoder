""" code 5.9

p87

calculate score of partition of an interval

"""
INF = 1 << 64 - 1


def main():
    N = int(input())
    c = [[] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            c[i][j] = int(input())

    # definition of dp table
    dp = [INF] * (N + 1)

    # initialize of dp
    dp[0] = 0

    # loop of dp
    for i in range(N + 1):
        for j in range(N + 1):
            dp[i] = min(dp[i], dp[j] + c[j][i])


if __name__ == "__main__":
    main()
