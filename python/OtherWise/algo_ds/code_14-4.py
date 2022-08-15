import heapq
from typing import List, NamedTuple, Tuple

INF = 1 << 60


class Edge(NamedTuple):
    to: int
    w: int


Graph = List[List[Edge]]


def main():
    n, m, s = map(int, input().split())

    g: Graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        g[a].append(Edge(to=b, w=w))

    # dijkstra
    dist = [INF] * n
    dist[0] = 0

    # make heap of pairs of (d[v], v)
    que: List[Tuple[int, int]] = []
    heapq.heapify(que)

    heapq.heappush(que, (dist[s], s))

    while not len(que):
        vd = heapq.heappop(que)
        v = vd[0]
        d = vd[1]

        if d > dist[v]:
            continue

        for e in g[v]:
            dist[e.to] = min(dist[e.to], dist[v] + e.w)
            if dist[e.to] == dist[v] + e.w:
                heapq.heappush(que, (dist[e.to], e.to))

    for v in range(n):
        if dist[v] < INF:
            print(dist[v])
        else:
            print("INF")


if __name__ == "__main__":
    main()
