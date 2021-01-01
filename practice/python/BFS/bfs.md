# BFS(幅優先探索)

DFSと同様にグラフを以下の形で使う

```python
from typing import List

Graph = List[List[int]]
```

BFSではキューを用いて実現する。

DFSはpythonでは普通のリストの扱いでスタックになっていたからあまり気にしなかった。

pythonでは`deque`を使う

実現のために以下のデータ構造を使う

()内はpython
|データ構造|使用した変数名|説明|
|-|-|-|
|vector(List)|dist|dist[v]はスタート頂点から頂点vまで何ステップで到達できるかを表す
|queue(deque)|que|その時点での橙色頂点（発見済みだが未訪問な頂点）を格納するキュー

[BFSの実装テンプレ]

```python
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
    while not que.empty():
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

```

- appendleft は左端に追加する。
- 今回はappendを使う（cppのque.push(a)と等価)

## 計算量

グラフの頂点数をN、辺の数をMとすると

- 各頂点はキューに高々１回挿入され、高々１回取り出されるので、その分の計算量がO(N)
- 各辺は高々１回だけ探索されることになるのでその分の計算量がO(M)

線形時間で合わせてO(N+M)程度の計算量になる。

## BFS 応用例

- 特徴：最短経路を求めることができるアルゴリズム

典型的な応用例
- パズルを解くための最小手数を求める
- FaceBookの友達関係などにおいて、ある人からある人へ何ステップで行けるかを求める


## 参考

- [BFS @drken](https://qiita.com/drken/items/996d80bcae64649a6580)

- [note.nkmk.me deque](https://note.nkmk.me/python-collections-deque/)

- []