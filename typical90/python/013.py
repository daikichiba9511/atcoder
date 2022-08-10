import heapq
from typing import List, Tuple


def dijkstra_heap(start: int, n: int, edges: List[List[Tuple[int, int]]]) -> List[int]:
    """heapqをつかった重みつきグラフのダイクストラ法

    Args:
        start: 探索を開始するノードのindex
        n: nodeの数
        edgeslist:
    """
    init_v = 1 << 64 - 1
    dist = [init_v] * (n + 1)
    dist[start] = 0

    # [(cost, to)]
    edgeslist = []
    heapq.heappush(edgeslist, (0, start))

    while len(edgeslist):
        # 最小値をpop , O(logN)
        # 何も指定しなければ優先度は0番目の要素
        pos = heapq.heappop(edgeslist)[1]
        for to, cost in edges[pos]:
            # コストの最小値が更新できるなら更新して、次の探索点の候補に入れる
            if dist[to] > dist[pos] + cost:
                dist[to] = dist[pos] + cost
                heapq.heappush(edgeslist, (dist[to], to))
    return dist


def main():
    N, M = list(map(int, input().split()))
    adjacent_list = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        adjacent_list[a - 1].append((b - 1, c))
        adjacent_list[b - 1].append((a - 1, c))

    # 頂点１からの最短距離
    dist1 = dijkstra_heap(0, N - 1, adjacent_list)

    # 頂点Nからの最短距離
    distN = dijkstra_heap(N - 1, N - 1, adjacent_list)

    for i in range(N):
        print(dist1[i] + distN[i])


if __name__ == "__main__":
    main()
