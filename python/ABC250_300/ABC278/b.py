H, M = map(int, input().split())

for h in range(H, 48):
    if h == H:
        start = int(M)
    else:
        start = 0

    for m in range(start, 60):
        if h < 10:
            a, b = 0, h % 24
        else:
            h = h % 24
            a, b = h // 10, h % 10

        if m < 10:
            c, d = 0, m % 60
        else:
            m = m % 60
            c, d = m // 10, m % 10

        if 0 <= b <= 5 and 0 <= c <= 9:
            if a == 2 and c < 4:
                print(f"{a}{b} {c}{d}")
                exit()
            elif a < 2:
                print(f"{a}{b} {c}{d}")
                exit()
