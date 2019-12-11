from typing import Iterable


def main()->None:
    # 回答見た。
    # よくわかってない。要復習、要研究。
    W, H, N = map(int, input().split())
    range_N: Iterable[int] = range(N)
    xl, xr, yd, yu = 0, W, 0, H
    for i in range_N:
        x, y, a = map(int, input().split())
        if a == 1:
            xl = max(x, xl)
        elif a == 2:
            xr = min(x, xr)
        elif a == 3:
            yd = max(y, yd)
        else:
            yu = min(y, yu)
    if xl >= xr or yd >= yu:
        print(0)
    else:
        print((xr - xl) * (yu - yd))

if __name__ == "__main__":
    main()