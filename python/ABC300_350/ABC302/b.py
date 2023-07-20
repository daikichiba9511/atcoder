h, w = map(int, input().split())
s = [input() for _ in [0] * h]


for i in range(h):
    for j in range(w):
        s_ij = s[i][j]
        if s_ij == "s":
            vertical1 = [(i, j - 1), (i, j - 2), (i, j - 3), (i, j - 4)]
            vertical2 = [(i, j + 1), (i, j + 2), (i, j + 3), (i, j + 4)]
            horizontal1 = [(i - 1, j), (i - 2, j), (i - 3, j), (i - 4, j)]
            horizontal2 = [(i + 1, j), (i + 2, j), (i + 3, j), (i + 4, j)]
            diagonal1 = [(i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3), (i - 4, j - 4)]
            diagonal2 = [(i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3), (i - 4, j + 4)]
            diagonal3 = [(i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3), (i + 4, j - 4)]
            diagonal4 = [(i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3), (i + 4, j + 4)]
            for d in [
                vertical1,
                vertical2,
                horizontal1,
                horizontal2,
                diagonal1,
                diagonal2,
                diagonal3,
                diagonal4,
            ]:
                d1, d2, d3, d4 = d
                if (
                    d1[0] >= h
                    or d2[0] >= h
                    or d3[0] >= h
                    or d4[0] >= h
                    or 0 > d1[0]
                    or 0 > d2[0]
                    or 0 > d3[0]
                    or 0 > d4[0]
                    or d1[1] >= w
                    or d2[1] >= w
                    or d3[1] >= w
                    or d4[1] >= w
                    or 0 > d1[1]
                    or 0 > d2[1]
                    or 0 > d3[1]
                    or 0 > d4[1]
                ):
                    continue

                if (
                    s[d1[0]][d1[1]] == "n"
                    and s[d2[0]][d2[1]] == "u"
                    and s[d3[0]][d3[1]] == "k"
                    and s[d4[0]][d4[1]] == "e"
                ):
                    print(f"{i+1} {j+1}")
                    for d_i, d_j in d:
                        print(f"{d_i+1} {d_j+1}")
                    exit()
