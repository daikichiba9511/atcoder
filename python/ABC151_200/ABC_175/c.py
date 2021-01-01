
def main():
    x, k, d = map(int, input().split())
    # x > 0
    if x < 0:
        x = -1 * x
    #the number of d in x
    r = abs(x) // d
    k_rest = k - r
    if r > 0 and k_rest < 0:
        print(x - k * d)
        exit()

    x_r = x - d * r
    x_l = x_r - d

    # print(f"xr: {x_r}\nxl: {x_l}\nk: {k_rest}")

    if k_rest % 2 == 0:
        print(abs(x_r))
    else:
        print(abs(x_l))

if __name__ == "__main__":
    main()
