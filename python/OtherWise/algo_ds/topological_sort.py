from typing import List

Graph = List[List[int]]

SEEN: List[bool] = []
ORDER: List[int] = []


def rec(g: Graph, v: int) -> None:
    SEEN[v] = True
    for next_v in g[v]:
        if SEEN[next_v]:
            continue
        rec(g, next_v)

    # record v-out
    ORDER.append(v)


def main() -> None:
    n, m = map(int, input().split())
    g: Graph = []
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)

    for _ in range(n):
        SEEN.append(False)
    ORDER.clear()
    for v in range(n):
        if SEEN[v]:
            continue
        rec(g, v)

    ORDER.reverse()

    for v in ORDER:
        print(v, end="->")
