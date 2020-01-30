


def tmp():
    a, b, x = map(int, input().split())
    count = 0
    for i in range(a, b+1):
        if i % x == 0:
            count += 1
    print(count)


def f(n, x):
    if n == -1:
        return 0
    else:
        return n // x + 1



def main():
    # 解説みた
    a, b, x = map(int, input().split())

    res = f(b, x) - f(a - 1, x)

    print(res)
if __name__ == "__main__":
    main()