"""
dp[i] = いくつかの区間に分割した時の区間の平均値の最大値
"""

import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    a = np.array(list(readline().decode()[:-1].split()), "int32")

    # [j, i)の平均値の前処理
    f = np.zeros((N + 1, N + 1), "float32")
    for i in range(1, N + 1):
        for j in range(i):
            f[j, i] = np.mean(a[j: i])

    # dp loop
    # TODO: ここの処理が遅いのでnumpyで高速化したい
    INF = 1 << 29
    dp = np.full((N + 1, M + 1), -INF, "float32")
    dp[0, 0] = 0
    for i in range(N + 1):
        for j in range(i):
            for k in range(1, M + 1):
                dp[i][k] = max(dp[i][k], dp[j][k - 1] + f[j, i])

    print(dp[N, :].max())


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print(f"elapsed time: {time.time() - start}")
