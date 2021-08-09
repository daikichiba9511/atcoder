""" Nからk個選んでWを作れるか

方針：分割統治でその和になる整数の個数の最小値を足していったときに最終的にk以下になっているか

Input Example

* sample1: No

```
3 5 2
1
1
2
```
* sample2: Yes

```
5 7 4
1
1
2
2
3
```

"""


def main():
    INF = 1 << 29
    N, W, k = map(int, input().split())
    a = [int(input()) for _ in range(N)]

    # 最初のi個の整数の中からいくつか選んだ総和がjになる方法のうち選ぶ整数の個数の最小値
    dp = [[INF] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(W + 1):
            # case1: a[i] is NOT selected
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

            # case2: a[i] is selected
            if j >= a[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a[i]] + 1)

    if dp[N][W] <= k:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
