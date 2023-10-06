n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

def score_fn(ometes, uras):
    return abs(sum(ometes)) + abs(sum(uras))


# (表の総和を正, 表の総和を負) x (裏の総和を正, 裏の総和を負)の4通りを全探索する
ans = 0
for i in range(4):
    if i == 0:
        # 表の総和を正, 裏の総和を正
        ometes, uras = [], []
        for a, b in ab:
            if a + b > 0:
                ometes.append(a)
                uras.append(b)
        ans = max(ans, score_fn(ometes, uras))
        pass
    elif i == 1:
        # 表の総和を正, 裏の総和を負
        ometes, uras = [], []
        for a, b in ab:
            if a - b > 0:
                ometes.append(a)
                uras.append(b)
        ans = max(ans, score_fn(ometes, uras))

    elif i == 2:
        # 表の総和を負, 裏の総和を正
        ometes, uras = [], []
        for a, b in ab:
            if -a + b > 0:
                ometes.append(a)
                uras.append(b)
        ans = max(ans, score_fn(ometes, uras))
    else:
        # 表の総和を負, 裏の総和を負
        ometes, uras = [], []
        for a, b in ab:
            if -a - b > 0:
                ometes.append(a)
                uras.append(b)
        ans = max(ans, score_fn(ometes, uras))
print(ans)
