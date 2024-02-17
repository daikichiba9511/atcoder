n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    ui, vi = map(int, input().split())
    graph[ui - 1].append(vi - 1)

# union-find
parent = [i for i in range(n)]
size = [1] * n


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        size[x] += size[y]


def same(x, y):
    return find(x) == find(y)


def group_size(x):
    return size[find(x)]


for v in range(n):
    for u in graph[v]:
        if v == 0:
            continue
        else:
            unite(u, v)

print(n - max(group_size(i) for i in range(n)))
