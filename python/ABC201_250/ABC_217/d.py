import bisect

L, Q = map(int, input().split())

cx = []
for _ in range(Q):
    cx.append(tuple(map(int, input().split())))

ans = list(range(L))

idx = []
for c_i, x_i in cx:
    if c_i == 1:
        idx.append(x_i)
        idx.sort()
    else:
        if idx == []:
            print(len(ans))
            continue
        start_idx = bisect.bisect_left(idx, x_i)
        end_idx = start_idx + 1
        if end_idx > len(idx):
            end_idx = len(ans) - 1

        print("start_idx:", start_idx, "end_idx:", end_idx, "x_i", x_i)
        print(len(ans[start_idx: end_idx]) + 1)
