def solve():
    n = int(input())
    lr = []
    for _ in range(n):
        lr.append(tuple(map(int, input().split())))

    # 計算量:O(NlogN)
    lr.sort(key=lambda x: x[1])
    res = 0
    current_time = 0
    for l, r in lr:
        if current_time > l:
            continue
        else:
            res += 1
            current_time = r
    print(res)

solve()


