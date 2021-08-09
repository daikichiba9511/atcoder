"""
sample1:
    12 43 7 15 9

ans1:
    2 4 0 3 1
"""


def binary_search(a, key):
    left = 0
    right = len(a) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if key > a[mid]:
            left = mid + 1
        elif key < a[mid]:
            right = mid - 1
        else:
            assert key == a[mid]
            return mid
    return -1


def main():
    a = list(map(int, input().split()))
    res = []
    for i in a:
        index = binary_search(sorted(a), key=i)
        res.append(index)
    print(res)


if __name__ == "__main__":
    main()
