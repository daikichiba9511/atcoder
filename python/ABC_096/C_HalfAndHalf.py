from typing import Iterable

def main()->None:
    a, b, c, x, y = map(int, input().split())

    range_i: Iterable[int] = range(0, 100001)
    min_z: int = 1000000000
    for i in range_i:
        z = i * (2 * c) + (max(0, x - i) * a) + (max(0, y - i) * b)
        if z < min_z:
            min_z = z
    print(min_z)


if __name__ == "__main__":
    main()