# 再帰関数をつかって解く
import sys


sys.setrecursionlimit(10000000)


n, m = map(int, input().split())
g = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

seen = [False] * n


def dfs(v):
    seen[v] = True
    for v_i in g[v]:
        if not seen[v_i]:
            dfs(v_i)


dfs(0)
# print(seen)
print("The graph is connected." if all(seen) else "The graph is not connected.")
