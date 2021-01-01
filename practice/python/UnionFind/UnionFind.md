# UnionFind

union-find木とはグループ分けを木構造で管理するデータ構造

同じグループに属する＝同じ木に属する

以下の２点を高速に行えるのがメリット

- 要素xと要素yが同じグループに属するかどうかを判定したい

ー> 要素xの根と要素yの根が同じならば同じグループ、要素xの根と要素yの根が同じでないならば異なるグループにあることがわかる

- 要素xと要素yが同じグループに属する場合、要素xの属するグループと要素yの属するグループの併合する

```python
from typing import List, Union
Num = Union[int, float]
Vector = List[int, float]


class UnionTree(object):
    def __init__(self):
        self._par : List[int] = None

    def __call__(self, N : int):
        """
        最初に全てが根だとして初期化する
        """
        self._par : List[int] = [i for i in range(N)]

    def root(self, x : int):
        """
        データxが属する木の根を再帰で得る:root(x)={xの木の根}
        """
        if self._par[x] == x:
            return x
        return self._par[x] = root(par[x])

    def unite(x : int, y : int):
        """
        xの木とyの木を併合
        """
        rx : int = root(x)
        ry : int = root(y)
        if rx == ry : # 等しければ何もせず抜ける
            return　pass
        self._par[rx] = ry

    def same(x : int, y : int)->bool:
        """
        xとyが同じならboolを返す
        """
        rx : int = root(x)
        ry : int = root(y)
        return rx == ry
```

example

```python

def main():
    n, m = map(int, input().split())

    tree = UnionFind()
    tree = tree(n)

    for _ in range(m):
        x, y = map(int, input().split())
        tree.unite(x-1, y-1)

    cnt = 0
    for i in range(n):
        if not tree.same(0, i):
            tree.unite(0, i)
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()

```