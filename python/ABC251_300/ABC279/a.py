H, W = map(int, input().split())
S = [[s for s in input() if s == "#"] for _ in range(H)]
print(sum([len(s) for s in S]))
