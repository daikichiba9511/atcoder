x, y = map(int, input().split())
res = [(x, y)]
# cnt = 0
while True:
    if (x, y) == (1, 1):
        break

    res.append((x, y))

    l = abs(x - y)
    if x > y:
        x = l
    else:
        y = l

    # print(res, x, y, l)
    # cnt += 1
    # if cnt > 4:
    #     break


for i in range(len(res), 1, -1):
    print(*res[i - 1])

