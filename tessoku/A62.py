n, m = map(int, input().split())
g = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


# これがすべてTrueなら連結グラフ
seen = [False] * n
todo = [0]

while todo:
    v = todo.pop()
    seen[v] = True
    for u in g[v]:
        if not seen[u]:
            todo.append(u)

print("The graph is connected." if all(seen) else "The graph is not connected.")
