# definition type hinting
from typing import List, Union
Num = Union[int, float]
Vector = List[int]


def binarySearch(list : Vector, item : int):
    # low と highリストの検索部分を探索
    low = 0
    high = len(list) - 1

    while low <= high:
        mid : int = (low + high) // 2
        guess : int = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def test_binarySearch():
    test_list = [1, 3, 5, 7, 9]
    print(binarySearch(test_list, 3))
    print(binarySearch(test_list, -1))

if __name__ == "__main__":
    test_binarySearch()