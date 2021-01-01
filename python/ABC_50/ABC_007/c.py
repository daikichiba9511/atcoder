# 重みなしグラフの最短経路問題はBFSで解ける
# 先入先出し　=> queue . python ならlistで大丈夫。list.pop(0) -> O(n)
from typing import List

Graph = List[str]

import sys
def main():
    def input(): return sys.stdin.readline()[:-1]

    R, C = map(int, input().split())
    sy, sx = map(int, input().split()) # start
    gy, gx = map(int, input().split()) # goal

    sx -= 1
    sy -= 1
    gy -= 1
    gx -= 1

    # receive input as Graph
    graph : Graph = [input() for _ in range(R)]

    # for BFS
    # Initialize all node by -1 which means not ariving
    dist = [[-1] * 50 for _ in range(50)]
    queue = [(sy, sx)]

    # start cordinate
    dist[sy][sx] = 0

    # run BFS (continue seeking if queue is not empty)
    while queue:
        vy, vx = queue.pop(0)

        if (vx, vy) == (gx, gy):
            break

        # survey all node we can achive.
        dxdy = [(1,0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in dxdy:
            if ( vx + dx > C ) or ( vy + dy > R) : continue
            if ( vx + dx < 0 ) or ( vy + dy < 0 ) : continue
            
            # ok
            elif graph[vy + dy][vx + dx] == ".":
                if dist[vy + dy][vx + dx] == -1:
                    queue.append((vy + dy, vx + dx))
                    dist[vy + dy][vx + dx] = dist[vy][vx] + 1
                else: continue
            # no
            elif graph[vy + dy][vx + dx] == "#": continue
    print(dist[gy][gx])

if __name__ == '__main__':
    main()
