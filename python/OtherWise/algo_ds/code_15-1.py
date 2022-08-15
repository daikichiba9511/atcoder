from typing import List, Tuple

# {w(e), {u, v}} represents e = (u, v)
Edge = Tuple[int, Tuple[int, int]]


class UnionFind:
    def __init__(self, n: int) -> None:
        assert isinstance(n, int)
        self._par = [-1] * n
        self._siz = [1] * n

    def root(self, x: int) -> int:
        if self._par[x] == -1:
            return x
        else:
            self._par[x] = self.root(self._par[x])
            return self._par[x]

    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self._siz[x] < self._siz[y]:
            x, y = y, x

        self._par[y] = x
        self._siz[x] += self._siz[y]
        return True

    def size(self, x: int) -> int:
        return self._siz[self.root(x)]


def main():
    n, m = map(int, input().split())

    edges: List[Edge] = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, (u, v)))

    edges.sort(key=lambda x: x[0])

    # Kruskal
    res = 0
    uf = UnionFind(n)
    for i in range(m):
        w = edges[i][0]
        u = edges[i][1][0]
        v = edges[i][1][1]

        if uf.issame(u, v):
            continue

        res += w
        uf.unite(u, v)

    print(res)


if __name__ == "__main__":
    main()
