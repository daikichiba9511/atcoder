# from __future__ import annotations

from itertools import permutations

n = int(input())
a = []
for i in range(n):
    a_i = tuple(map(int, input().split()))
    a.append(a_i)

p = [i for i in range(n)]

m = int(input())
bad_list = [[False] * 10 for _ in range(10)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad_list[x][y] = True
    bad_list[y][x] = True

ans = 1 << 30
# O(N! * N)
# 制約が小さいときに、順列全探索
for perm in permutations(range(n), n):
    s = 0
    flag = False
    # iとi+1の仲が悪いなら不適な順列
    for interval_idx in range(n - 1):
        if bad_list[perm[interval_idx]][perm[interval_idx + 1]]:
            flag = True
    if flag:
        continue

    for interval_idx in range(n):
        s += a[perm[interval_idx]][interval_idx]
    ans = min(ans, s)

if ans == 1 << 30:
    print("-1")
else:
    print(ans)

