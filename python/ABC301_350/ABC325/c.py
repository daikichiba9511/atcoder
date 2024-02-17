class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


h, w = map(int, input().split())
s = [[s_i for s_i in input() ] for _ in range(h)]
# print(s)

# cencerに事前にidを降っておく
# O(h*w)
cencer_cnt = 0
cencer_pos = {}
for i, s_i in enumerate(s):
    for j, e in enumerate(s_i):
        if e == "#":
            cencer_pos[(i, j)] = cencer_cnt
            cencer_cnt += 1

# print(cencer_pos)

uf = UnionFind(cencer_cnt)
# 1<=h,w<=1000
# O(hw)
for i in range(h):
    for j in range(w):
        s_ij = s[i][j]
        if s_ij != "#":
            continue

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            if not (0 <= i + y < h and 0 <= j + x < w):
                continue

            xprime = j + x
            yprime = i + y
            sprime = s[yprime][xprime]
            if sprime == "#":
                ij_idx = cencer_pos[(i, j)]
                xy_idx = cencer_pos[(yprime, xprime)]
                uf.union(ij_idx, xy_idx)
print(uf.group_count())


