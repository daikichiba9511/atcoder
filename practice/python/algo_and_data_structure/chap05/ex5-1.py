"""

dp[i] := i 日目での幸福度の最大値

Reference:
    * [1] https://atcoder.jp/contests/dp/tasks/dp_c?lang=ja

"""
import numpy as np


def main():
    N = int(input())
    abc = []
    for _ in range(N):
        abc.append(tuple(map(int, input().split())))

    # definition of dp table and initialize
    dp = [0] * N

    # loop of dp
    previous = -1
    for i in range(N):
        for j in range(3):
            larger = np.sort(abc[i])[::-1][j]
            if j != previous:
                dp[i] = max(dp[i], dp[i - 1] + larger)
                previous = j
                break
            else:
                continue

    print(dp[N - 1])


if __name__ == "__main__":
    main()
