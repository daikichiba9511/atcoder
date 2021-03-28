import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    n = int(input())

    ans = 0
    if n >= 10 ** 3:
        ans += n - 999
    if n >= 10 ** 6:
        ans += n - 999_999
    if n >= 10 ** 9:
        ans += n - 999_999_999
    if n >= 10 ** 12:
        ans += n - 999_999_999_999
    if n >= 10 ** 15:
        ans += n - 999_999_999_999_999

        print(ans)


if __name__ == "__main__":
    main()
