import heapq

INF = 10 ** 18

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))


que = []
kakutei = [False] * n
cur = [INF] * n
cur[0] = 0
heapq.heappush(que, (cur[0], 0))

# dijkstra
while que:
    # 次に確定させるべき頂点を求める
    pos = heapq.heappop(que)[1]

    # Queueの最小要素がすでに確定している場合は無視する
    if kakutei[pos]:
        continue

    # cur[x]の値を確定させる
    kakutei[pos] = True
    for nex, cost in g[pos]:
        if cur[nex] > cur[pos] + cost:
            cur[nex] = cur[pos] + cost
            heapq.heappush(que, (cur[nex], nex))

for i in range(n):
    if cur[i] == INF:
        print(-1)
    else:
        print(cur[i])
