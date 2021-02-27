import sys

def binary_search_max(d: int, m: int, x: int) -> int:
    """ 二分探索でf(n)<=mを満たす最大のnを探索する
    """
    low = 0
    candidate = [i for i in range(d + 1, 36)]
    high = len(candidate) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = candidate[mid]
        conveted_number = int(str(x), guess)

def main():
    def input():
        return sys.stdin.readline()[:-1]

    x = input()
    m = int(input())
    d = max(sorted(str(x), reverse=True))

    res = binary_search_max(int(d), int(m), int(x))
    print(res)


if __name__ == "__main__":
    main()
