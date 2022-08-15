from typing import Final, List

INF: Final[int] = 1 << 60


def main():
    n, m = map(int, input().split())
    dp = [[INF] * n for _ in range(n)]

    for e in range(m):
        a, b, w = map(int, input().split())
        dp[a][b] = w

        for v in range(n):
            dp[v][v] = 0

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    exist_negative_cycle = False
    for v in range(n):
        if dp[v][v] < 0:
            exist_negative_cycle = True

    if exist_negative_cycle:
        print("NEGATIVE CYCLE")

    else:
        for i in range(n):
            for j in range(n):
                if j:
                    print(" ")
                if dp[i][j] < INF / 2:
                    print(dp[i][j])
                else:
                    print("INF")
