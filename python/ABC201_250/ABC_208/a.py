import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    a, b = map(int, input().split())

    if (b <= 600) and (6 * a >= b) and (a <= b):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
