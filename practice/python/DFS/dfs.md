# 深さ優先探索

https://qiita.com/drken/items/4a7869c5e304883f539b

## graph template

```python

from typing import List
Graph = List[List[int]]

def main():
    # 頂点数と辺数
    N : int = int(input())
    M : int = int(input())

    #　グラフ
    G : Graph = [[] * N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

        # 無向グラフの場合は以下を追加
        # G[b].append(a)

```

### have weight in Edge

辺に重みを持っている場合

```python

from typing import List
Graph = List[List[int]]
Vector = List[int]

class Edge(object):
    def __init__(self, to : Vector, weight : Vecotr):
        # 辺の重み
        self._weight = weight
        # 辺の行先
        self._to = to

    def __call__(self, t : int, w : int):
        return self._to[t], self._weight[w]

def main():
    # 頂点数と辺数
    N : int = int(input())
    M : int = int(input())

    #　グラフ
    G : Graph = [[0] * N for _ in range(N)]
    for i in range(M):
        begin, end, weight = map(int, input().split())
        G[begin].append(Edge(end, weight))

```

- seen: その頂点を検知済みかどうかを表す配列
- todo: 検知したけどまだ訪れてない頂点の集合

これらを管理することで探索する

```

1. seen全体をFalseで初期化してtodoをからにする
2. seed[s] = trueとして、todoにsを追加する
3. todoが空になるまで以下を繰り返す
4. todoから一つ取り出してvとする。
5. T(v)の各要素wに対して
6.   seen[w]=Trueならば何もしない
7.   otherwiseならseen[w] = True にしてtodoにwをつい明日る。

```

todoに追加したやつから、

- 1.元々あった方から読むのか
- 2.後から追加された方を読むのか

２通りの方針がある。

1 ならば　スタック（深さ優先探索）
2 ならば　キュー　（幅優先探索）

を使うことで実装することができる

根を探索の始点とするのが自然

DFSは再起関数と相性が良い。

### DFS template

```python
from typing import List
Graph = List[List[int]]

# 深さ優先探索
seen : List[bool] = [False] * N
def dfs(G : Graph, v : int):
    # vを訪問済みにする
    seen[v] = True

    # vから行ける各頂点 next_v について
    for next_v in G[v]:
        if seen[next_v] : continue # next_v が探索済みならスルー
        dfs(G, next_v) # 再帰的に探索

def main():
    # 頂点数と辺数
    N : int = int(input())
    M : int = int(input())

    #　グラフ
    G : Graph = [[] * N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 頂点０をスタートとして探索
    dfs(G, 0)
```

トポロジカルソートや強連結成分分解はDFSの応用らしい。

行きがけ順と帰りがけ順

