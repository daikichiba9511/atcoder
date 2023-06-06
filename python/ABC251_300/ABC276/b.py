N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b)
    g[b - 1].append(a)

for g_i in g:
    if not g_i:
        print("0")
    else:
        print(f"{len(g_i)} " + " ".join(map(str, sorted(g_i))))
