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


n, m = map(int, input().split())
edges = []
a = []
b = []
for i in range(m):
    ai, bi, ci = map(int, input().split())
    edges.append((ci, i))
    a.append(ai)
    b.append(bi)

edges.sort(key=lambda x: x[0])

uf = UnionFind(n + 1)
ans = 0

for i in range(len(edges)):
    idx = edges[i][1]
    # 同じルートの属してなければ、それを選んで重みを足す
    if not uf.issame(a[idx], b[idx]):
        uf.unite(a[idx], b[idx])
        ans += edges[i][0]
print(ans)
