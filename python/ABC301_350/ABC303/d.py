x, y, z = map(int, input().split())
s = input()

n = len(s)
INF = 10 ** 18

# i,0 = off, i,1 = on
dp = [[INF] * 2 for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    # the cost of changing capslock 0/1
    # At ith step, the minimum cost of 0
    dp[i][0] = min(dp[i][0], dp[i][1] + z)
    dp[i][1] = min(dp[i][1], dp[i][0] + z)

    if s[i] == "a":
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + x)  # OFF
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + y)  # ON
    else:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + y)  # OFF
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + x)  # ON

print(min(dp[n][0], dp[n][1]))
