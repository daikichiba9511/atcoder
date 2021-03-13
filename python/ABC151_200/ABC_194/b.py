import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    a, b, w = map(int, input().split())
    min_ = 10 ** 9
    max_ = 0
    for n in range(1, 10 ** 6 + 1):
        if (a * n <= 1000 * w) and (1000 * w <= b * n):
            min_ = min(min_, n)
            max_ = max(max_, n)

    if max_ == 0:
        print("UNSATISFIABLE")
    else:
        print(min_, max_)


if __name__ == "__main__":
    main()
