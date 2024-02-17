import collections

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


dist = [-1] * n
q = collections.deque()

q.append(0)
dist[0] = 0

while q:
    v = q.popleft()
    for vi in g[v]:
        if dist[vi] != -1:
            continue
        dist[vi] = dist[v] + 1
        q.append(vi)

for d in dist:
    print(d)
