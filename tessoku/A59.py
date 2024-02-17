class SegmentTree:
    inf: int = 10**18 + 1

    def __init__(self, n: int, bi_ope_type: str = "sum") -> None:
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [0] * (2 * self.size)
        self.bi_ope_type = bi_ope_type
        self._set_no_relative_value()

    def _set_no_relative_value(self) -> None:
        """二項演算の単位元を設定する"""
        if self.bi_ope_type == "sum":
            self.no_relative_value = 0
        elif self.bi_ope_type == "max":
            self.no_relative_value = -self.inf
        elif self.bi_ope_type == "min":
            self.no_relative_value = self.inf
        else:
            raise ValueError(f"bi_ope_type が不正です: {self.bi_ope_type}")

    def bi_ope(self, x: int, y: int) -> int:
        """二項演算の定義を行う関数"""
        if self.bi_ope_type == "sum":
            return x + y
        elif self.bi_ope_type == "max":
            return max(x, y)
        elif self.bi_ope_type == "min":
            return min(x, y)
        else:
            raise ValueError(f"bi_ope_type が不正です: {self.bi_ope_type}")

    def update(self, pos: int, x: int) -> None:
        """pos 番目の要素を x に更新"""
        # セルは右から更新していく
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
            return self.no_relative_value
        if left <= a and b <= right:
            return self.data[u]

        mid = (a + b) // 2
        ansl = self.query(left, right, a, mid, u * 2)
        ansr = self.query(left, right, mid, b, u * 2 + 1)
        return self.bi_ope(ansl, ansr)


n, q = map(int, input().split())

pos, x, left, right, query = (
    [0] * (10**6 + 1),
    [0] * (10**6 + 1),
    [0] * (10**6 + 1),
    [0] * (10**6 + 1),
    [0] * (10**6 + 1),
)
for i in range(1, q + 1):
    args = list(map(int, input().split()))
    if args[0] == 1:
        query[i], pos[i], x[i] = args
    else:
        query[i], left[i], right[i] = args

z = SegmentTree(n, bi_ope_type="sum")

for i in range(1, q + 1):
    qi = query[i]
    if qi == 1:
        z.update(pos[i], x[i])
    else:
        ans = z.query(left[i], right[i], 1, z.size + 1, 1)
        print(ans)
