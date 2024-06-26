n = int(input())
a = list(map(int, input().split()))
g = [[] for _ in range(n + 2)]
for i, ai in enumerate(a, 2):
    g[ai].append(i)

# dp[i] := i番目の社員の部下の数
# 直属の上司の番号は自分よりも小さく番号が大きいほうが部下になるのでN -> 1に向かって更新していけば良い
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    for vj in g[i]:
        # 上司iの部下の数=自分の部下の数+自分
        dp[i] += dp[vj] + 1

print(*dp[1:-1])
