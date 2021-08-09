""" code 5.8

P82

calculate Editing distance between S and T

"""
INF = 1 << 64 - 1


def main():
    S, T = input().split()

    # definition of dp table
    dp = [[INF] * (len(S) + 1) for _ in range(len(T) + 1)]

    # initialize dp table
    dp[0][0] = 0

    # loop of dp
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            # change operation
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            # delete operation
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            # insert operaion
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    print(dp[len(S)][len(T)])


if __name__ == "__main__":
    main()
