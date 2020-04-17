def main():
    H, W = map(int, input().split())
    S = [input().split() for _ in range(H)]
    dxdy = [(1,0), (0, 1), (-1, 0), (0, -1)]
    for h in range(H):
        for w in range(W):
            for dx, dy in dxdy:
                if h + dy < 0 or h + dy > H - 1 or w + dx < 0 or w + dx > W -1:
                    continue
                print(S[w+dx])




if __name__ == "__main__":
    main()