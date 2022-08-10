import itertools
N, M = map(int, input().split())

res = []
for c in itertools.permutations(range(1, M + 1), N):
    prev_i = 0
    ok = True
    for c_i in c:
        if c_i < prev_i:
            ok = False
            break
        prev_i = c_i

    if ok:
        res.append(c)

res.sort()
for r in res:
    print(" ".join(map(str, r)))
