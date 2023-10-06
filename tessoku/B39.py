def solve():
    n, d = map(int, input().split())
    xy = []
    for _ in range(n):
        xy.append(tuple(map(int, input().split())))

    xy.sort(key=lambda x: x[1], reverse=True)
    print(xy)

    # そのindexのしごとを使ったどうかの情報をもっておくことでpopを使わなくてもよくなる
    # popは最悪計算量がO(N)なので、使うと計算量がO(DN^2)になってしまう
    used = [False] * n

    # 計算量: O(DN) = O(10^5 * 10^3) = O(10^8)
    ans = 0
    for i in range(1, d + 1):
        for j in range(n):
            if used[j]:
                continue
            x, y = xy[j]
            if x <= i:
                ans += y
                used[j] = True
                break
        # print(f"{i=}, {ans=}")
        # print(f"{c=}")

    print(ans)


solve()
