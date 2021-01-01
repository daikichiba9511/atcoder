from collections import deque

from typing import List
Graph = List[List[int]]

def main():
    # 頂点数と辺数
    n, m = map(int, map(int, input().split()))

    # グラフ入力受け取り
    G : Graph = [[]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # BFSのためのデータ構造
    dist : List[int] = [-1]*n # 全頂点を未訪問に初期化
    que = deque()

    # 初期条件（頂点０を初期ノードとする）
    dist[0] = 0
    que.append(0)

    # BFS開始(queが空になるまで探索を続ける)
    while len(que) != 0:
        v : int = que.popleft() # queの左端から要素を取り出す
        # vから辿れる頂点を全て調べる
        for nv in G[v]:
            #すでに訪問済みの頂点は探索しない
            if dist[nv] != -1 : continue

            # 新たな白色頂点nvについて距離情報を更新してキューに追加する
            dist[nv] = dist[v] + 1
            que.append(nv)

    # 結果出力（各頂点の頂点　０　からの距離をみる
    for v in range(n):
        print(v, " : ", dist[v])

if __name__ == "__main__":
    main()