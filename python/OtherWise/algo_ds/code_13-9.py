from typing import List

Graph = List[List[int]]

DEPTH: List[int] = []
SUBTREE_SIZE: List[int] = []


def dfs(g: Graph, v: int, p: int = -1, d: int = 0) -> None:
    DEPTH[v] = d
    for c in g[v]:
        if c == p:
            continue
        dfs(g, c, v, d + 1)

    SUBTREE_SIZE[v] = 1
    for c in g[v]:
        if c == p:
            continue
        SUBTREE_SIZE[v] += SUBTREE_SIZE[c]


def main() -> None:
    n = int(input())
    g: Graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    root = 0
    for _ in range(n):
        DEPTH.append(0)
        SUBTREE_SIZE.append(0)

    dfs(g, root)

    for v in range(n):
        print(v, ": depth = ", DEPTH[v])
        print("subtree_size = ", SUBTREE_SIZE[v])
