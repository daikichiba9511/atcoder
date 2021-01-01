# 0-1BFSというのを使うとできるらしい
# ダイクストラでも解ける

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(list(map(int, input().split())))

    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in dxdy:
        if (Cw + dx - 1 > W) or (Cw + dx - 1 < 0):continue
        if (Ch + dy - 1 > H) or (Ch + dy - 1 < 0):continue

if __name__ == "__main__":
    main()