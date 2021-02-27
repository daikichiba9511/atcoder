import sys

def g_1(x: int) -> int:
    x = str(x)
    x = sorted(x, reverse=True)
    x = "".join(x)
    return int(x)

def g_2(x: int) -> int:
    x = str(x)
    x = sorted(x)
    x = "".join(x)
    return int(x)

def f(x: int) -> int:
    return g_1(x) - g_2(x)

def main():
    def input(): return sys.stdin.readline()[:-1]

    n, k = tuple(map(int, input().split()))
    for _ in range(k):
        n = f(n)
    print(n)

if __name__ == "__main__":
    main()
