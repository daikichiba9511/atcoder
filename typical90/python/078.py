N, M = map(int, input().split())

g = [[] for _ in range(M + 1)]
for _ in range(M):
    a_i, b_i = map(int, input().split())
    g[a_i - 1].append(b_i - 1)
    g[b_i - 1].append(a_i - 1)

res_cnt = 0
for a_i in range(len(g)):
    cnt = [j for j in g[a_i] if j < a_i]
    if len(cnt) != 1:
        continue
    res_cnt += 1

print(res_cnt)
