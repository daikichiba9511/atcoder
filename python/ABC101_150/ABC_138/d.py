import sys
from typing import List, Tuple
import collections

Graph = List[List[int]]


def main():
    def input(): return sys.stdin.readline()[:-1]
    N, Q = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(1, N):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    px = [0] * (N + 1)
    for _ in range(Q):
        p, x = map(int, input().split())
        px[p] += x

    queue = collections.deque()
    queue.append(1)
    checked = [0] * (N + 1)
    while queue:
        v = queue.pop()
        checked[v] = 1
        for next_v in graph[v]:
            if checked[next_v] == 1: continue
            px[next_v] += px[v]
            queue.append(next_v)
    print(*px[1:])

if __name__ == '__main__':
    main()

    