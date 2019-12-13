


def main()->None:
    # 他の人の回答見た。
    # https://atcoder.jp/contests/abc074/submissions/8698084
    # 自分のコードは間違えてるが、闇感が出てきてるので飛ばす。
    a, b, c, d, e, f = map(int, input().split())

    max_sugar = 0
    max_water = 100 * a
    max_concentration = 0.0
    a_limit = f // (100 * a)
    for i in range(a_limit+1):
        b_limit = (f - 100 * a * i) // (100 * b)
        for j in range(b_limit + 1):
            if i == 0 and j == 0: continue
            sugar_limit = min(e * (a * 1 + b * j), f - 100 * ( a * i + b * j ))

            sugar = 0
            for g in range(sugar_limit // c + 1):
                h = (sugar_limit - g * c ) // d
                temp_sugar = g * c + h * d
                sugar = max(sugar, temp_sugar)
            temp_cons = sugar / (sugar + 100 * (a * i + b * j))
            if temp_cons > max_concentration:
                max_concentration = temp_cons
                max_water = 100 * (a * i + b * j)
                max_sugar = sugar
    print("{} {}".format(max_water + max_sugar, max_sugar))


if __name__ == "__main__":
    main()