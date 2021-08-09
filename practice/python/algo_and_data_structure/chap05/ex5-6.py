""" N 個の数からそれぞれ選べる数が決まってる中で総和をWに一致させられるか

dp[i][j] := 最初のi個の整数のみを用いて、整数jを作る場合のうち、最後の整数を用いる回数の最小値

"""


def main():
    INF = 1 << 29
    N, W = map(int, input().split())
    a = []
    m = []
    for _ in range(N):
        a_, m_ = map(int, input().split())
        a.append(a_)
        m.append(m_)

    dp = [[INF] * (W + 1) for _ in range(N)]
    dp[0][0] = 1

    for i in range(1, N):
        for j in range(W + 1):
            # case1: a[i] is NOT selected
            dp[i + 1][j] = min(dp[i + 1][j], 0)

            # case2: a[i] is selected
            if j >= a[i] and dp[i + 1][j - a[i]] < m[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - a[i]] + 1)

    if dp[N][W] < INF:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
