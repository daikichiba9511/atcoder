n, m = map(int, input().split())
g = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for i, vs in enumerate(g, 1):
    vs = map(lambda x: x + 1, vs)
    vs = "{" + ", ".join(map(str, vs)) + "}"
    print(f"{i}: {vs}")
