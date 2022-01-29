import math
import bisect
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]


def getangle(xy_i):
    # cos(theta) = x / (x^2 + y^2)^{1/2}
    cos = xy_i[0] / ((xy_i[0] ** 2 + xy_i[1] ** 2) ** (1/2))
    theta = math.acos(cos) * 180.0 / math.pi
    if xy_i[1] >= 0.0:
        return theta
    return 360.0 - theta


def getangle2(x, y):
    diff = abs(x - y)
    if diff >= 180.0:
        return 360.0 - diff
    return diff


def solve(pos, pts, n):
    v = []
    for i in range(n):
        # posは固定した点Bだから同じ点のy=y_posとの偏角は0なのでするー
        if i == pos:
            continue
        sa = (pts[i][0] - pts[pos][0], pts[i][1] - pts[pos][1])
        angle = getangle(sa)
        v.append(angle)
    v.sort()

    ret = 0.0
    for i in range(len(v)):
        target = v[i] + 180.0
        if target >= 360.0:
            target -= 360.0
        pos1 = bisect.bisect_left(v, target)

        # 点Cの候補はたかだか２つにしぼれる
        cand1_idx = pos1 % len(v)
        cand2_idx = (pos1 + len(v) - 1) % len(v)
        cand1 = getangle2(v[i], v[cand1_idx])
        cand2 = getangle2(v[i], v[cand2_idx])
        ret = max([ret, cand1, cand2])
    return ret


ans = 0.0
for i in range(n):
    ans = max(ans, solve(i, xy, n))
print(ans)
