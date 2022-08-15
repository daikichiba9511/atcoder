from typing import List, NamedTuple

INF = float("inf")


class Edge(NamedTuple):
    to: int
    w: int


Graph = List[List[Edge]]


def main() -> None:
    n, m, s = map(int, input().split())

    g: Graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        g[a].append(Edge(to=b, w=w))

    # Bellman-Ford
    # flag of whether hav negative cycle or not
    exist_nagative_cycle = False
    dist = [INF] * n
    dist[s] = 0

    for i in range(n):
        update = False
        for v in range(n):
            if dist[v] == INF:
                continue
            for e in g[v]:
                dist[e.to] = min(dist[e.to], dist[v] + e.w)
                if dist[e.to] == dist[v] + e.w:
                    update = True
        if not update:
            break

        if i == n - 1 and update:
            exist_nagative_cycle = True

    if exist_nagative_cycle:
        print("NEGATIVE_CYCLE")

    else:
        for v in range(n):
            if dist[v] < INF:
                print(dist[v])

            else:
                print("INF")
