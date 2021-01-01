import sys

from collections import deque


def main():
    def input(): return sys.stdin.readline()[:-1]
    H, W = map(int, input().split())

    graph = [input() for _ in range(H)]

    dist = [[-1] * W for _ in range(H)]
    queue = deque()

    H -= 1
    W -= 1
    
    # initialize
    queue.append((0, 0))
    dist[0][0] = 0
    cnt = 0
    for g in graph:
        cnt += g.count(".")

    while queue:
        vx, vy = queue.popleft()

        if (vx, vy) == (W, H):
            break

        dxdy = [(1,0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in dxdy:
            if (vx + dx > W) or (vy + dy > H): continue
            elif (vx + dx < 0) or (vy + dy < 0): continue

            elif graph[vy + dy][vx + dx] == ".":
                if dist[vy + dy][vx + dx] == -1:
                    queue.append((vx + dx, vy + dy))
                    dist[vy + dy][vx + dx] = dist[vy][vx] + 1

            elif graph[vy + dy][vx + dx] == "#": continue
            else: continue

    # can't goal
    if dist[H][W] == -1:
        print(-1)
    else:
        # the number of "." - min(dist) - "." of start
        print(cnt - dist[H][W] - 1)

if __name__ == '__main__':
    main()