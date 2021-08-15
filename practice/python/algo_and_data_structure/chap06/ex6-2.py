import bisect


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # O(NlogN)
    a.sort()
    b.sort()
    c.sort()

    res = 0
    for a_i in a:
        b_i = bisect.bisect_left(b, a_i)
        c_i = bisect.bisect_right(c, b_i)
        print(a_i, b_i, c_i)
        res += len(b) - b_i + len(c) - c_i - 2
    print(res)


if __name__ == "__main__":
    main()
