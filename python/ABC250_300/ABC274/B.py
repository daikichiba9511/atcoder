H, W = map(int, input().split())

grid = [[] for _ in range(H)]
for h in range(H):
    C = input()
    for c in C:
        grid[h].append(c)
res = []
for w in range(W):
    cnt = 0
    for h in range(H):
        symbol = grid[h][w]
        if symbol == "#":
            cnt += 1
    res.append(str(cnt))

print(" ".join(res))

