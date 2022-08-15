from typing import List, NamedTuple

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

    # dijgksstra
    # O(V^2): V is set of Edges
    used = [False] * n
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n):
        min_dist = INF

        # search a vertex that has shortest distance from a searched vertex
        min_v = -1
        for v in range(n):
            if not used[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v

        if min_v == -1:
            break

        for e in g[min_v]:
            # chmin
            dist[e.to] = min(dist[e.to], dist[min_v] + e.w)

        # report the vertex have been searched
        used[min_v] = True

    for v in range(n):
        if dist[v] < INF:
            print(dist[v])
        else:
            print("INF")
