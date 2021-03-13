import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    n = int(input())
    # a^bの形で表せるのを探すので最低でもa^2<=nでないと行けない
    # だから探索範囲はn**(0.5)まででいい
    sq = int(n ** 0.5)
    s = set()
    for a in range(2, sq + 1):
        x = a * a
        while x <= n:
            s.add(x)
            x *= a
    print(n - len(s))


if __name__ == "__main__":
    main()
