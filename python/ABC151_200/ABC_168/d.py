from collections import deque

from typing import List
Graph = List[List[int]]

def main():
    n, m = map(int, input().split())
    G : Graph = [[]*n for _ in range(m)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a-1].append(b)
        G[b-1].append(a)
    print(G)

    #距離の初期化
    limit = 10 ** 5
    dist = {i: limit+1 for i in range(1, n+1)}
    que = deque()

    # 初期条件
    dist[1] = 0
    que.append(1)
    ans = [0]*(n+1)

    # BFS開始
    while len(que) != 0:
        visit : int = que.popleft()

        for next_v in G[visit-1]:
            if dist[next_v] > dist[visit] + 1:
                # 新たな頂点next_vについて距離情報を更新してキューに追加する
                dist[next_v] = dist[visit] + 1
                que.append(next_v)
                ans[next_v] = visit

    if all([i != 0 for i in ans[2:]]):
        print("Yes")
        print(*ans[2:], sep="\n")
    else:print("No")

if __name__ == "__main__":
    main()