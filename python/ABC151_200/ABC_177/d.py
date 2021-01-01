import sys
from typing import List

class UnionFind:
    """
    自身が親であれば、その集合に属する頂点数に-1をかけた物
    そうでなければ、親のid
    """
    def __init__(self, r: int):
        self.r : List[int] = [-1] * r

    def root(self, x: int):
        if self.r[x] < 0: return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x: int, y: int)->bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.r[x] > self.r[y]:
            x, y = y, x
        self.r[x] += self.r[y]
        self.r[y] = x
        return True

    def size(self, x: int)->int:
        return -self.r[self.root(x)]

def main():
    def input(): return sys.stdin.readline()[:-1]
    n, m = map(int, input().split())
    
    # 友達集合を作る
    uf = UnionFind(n)
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        uf.unite(a, b)

    # 最大の友達集合をもとめる
    ans = 0
    for i in range(n):
        ans = max(ans, uf.size(i))

    print(ans)

if __name__ == "__main__":
    main()

