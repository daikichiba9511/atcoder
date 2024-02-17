class SegmentTree:
    def __init__(self, n: int) -> None:
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [0] * (2 * self.size)

    def bi_ope(self, x: int, y: int) -> int:
        """二項演算の定義を行う関数"""
        return max(x, y)

    def update(self, pos: int, x: int) -> None:
        """pos 番目の要素を x に更新"""
        pos = pos + self.size - 1
        self.data[pos] = x
        while pos >= 2:
            pos //= 2
            self.data[pos] = self.bi_ope(self.data[pos * 2], self.data[pos * 2 + 1])

    def query(self, left: int, right: int, a: int, b: int, u: int) -> int:
        """
        u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
        半開区間 [l, r) の最大値を求めるには、query(l, r, 1, self.size, 1) を呼び出せばいい
        """
        if right <= a or b <= left:
            return -100000000
        if left <= a and b <= right:
            return self.data[u]

        mid = (a + b) // 2
        ansl = self.query(left, right, a, mid, u * 2)
        ansr = self.query(left, right, mid, b, u * 2 + 1)
        return self.bi_ope(ansl, ansr)


n, q = map(int, input().split())
pos, x, l, r, query = (
    [0] * (10**5 + 1),
    [0] * (10**5 + 1),
    [0] * (10**5 + 1),
    [0] * (10**5 + 1),
    [0] * (10**5 + 1),
)
for i in range(1, q + 1):
    q0, q1, q2 = list(map(int, input().split()))
    if q1 == 1:
        query[i], pos[i], x[i] = q0, q1, q2
    else:
        query[i], l[i], r[i] = q0, q1, q2

z = SegmentTree(n)
for i in range(1, q + 1):
    if query[i] == 1:
        # セルの値を下から更新していく
        z.update(pos[i], x[i])
    if query[i] == 2:
        # 区間 [l, r) の最大値を求める
        ans = z.query(l[i], r[i], 1, z.size + 1, 1)
        print(ans)
