n, m, h, k = map(int, input().split())
s = input()
xy = {tuple(map(int, input().split())) for _ in [0] * m}

if n <= h:
    print("Yes")
else:
    now_hp = h
    now_coord = (0, 0)
    for i in range(len(s)):
        s_i = s[i]
        if s_i == "R":
            now_coord = (now_coord[0] + 1, now_coord[1])
        elif s_i == "L":
            now_coord = (now_coord[0] - 1, now_coord[1])
        elif s_i == "U":
            now_coord = (now_coord[0], now_coord[1] + 1)
        else:
            now_coord = (now_coord[0], now_coord[1] - 1)

        now_hp -= 1
        if now_hp < 0:
            print("No")
            exit()

        # x_i, y_i item check
        if now_coord in xy:
            if now_hp < k:
                now_hp = k
                # use item, so delete item from xy(item manage hash map)
                xy.remove(now_coord)

        # print(now_hp, now_coord)

    print("Yes")
