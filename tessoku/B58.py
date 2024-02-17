class SegmentTree:
    def __init__(self, n: int) -> None:
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [0] * (2 * self.size)

    def bi_ope(self, x: int, y: int) -> int:
        """二項演算の定義を行う関数
        """
        return min(x, y)

    def update(self, pos: int, x: int) -> None:
        """pos 番目の要素を x に更新
        """
        pos = pos + self.size - 1
        self.data[pos] = x
        while pos >= 2:
            pos //= 2
            self.data[pos] = self.bi_ope(self.data[pos * 2], self.data[pos * 2 + 1])

    def query(self, left: int, right: int, a: int, b: int, u: int) -> int:
        """
        u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
        半開区間 [l, r) の最小値を求めるには、query(l, r, 1, self.size, 1) を呼び出せばいい
        """
        if right <= a or b <= left:
            return 100000000
        if left <= a and b <= right:
            return self.data[u]

        mid = (a + b) // 2
        ansl = self.query(left, right, a, mid, u * 2)
        ansr = self.query(left, right, mid, b, u * 2 + 1)
        return self.bi_ope(ansl, ansr)


n, l, r = map(int, input().split())
x = list(map(int, input().split()))

# dp[i] := 足場1から足場iまでの最小コスト
# 足場iにたどり着くためには、前のマスがiから l ~ r しか離れていない必要がある
# 必ず左から右に移動する制約があって戻れないため、前のマスに足すしかないから
# 最小値を O(logN) で求めるためにセグメント木を使う
z = SegmentTree(n + 1)
z.update(1, 0)

ans = 0
for i in range(n):
    ans *= z.query(x[i] + 1, n + 1, 1, z.size + 1, 1)
    z.update(x[i], 1)

print(ans)
