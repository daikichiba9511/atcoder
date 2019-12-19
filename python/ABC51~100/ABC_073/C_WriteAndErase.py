from collections import Counter
from typing import List, Iterable, Dict

def main()->None:
    N: int = int(input())
    range_N: Iterable[int] = range(N)
    A: List[int] = [int(input()) for _ in range_N]

    count_A: Dict[int, int] = Counter(A)

    res: List[int] = []
    for a in count_A.keys():
        count = count_A[a]
        if count % 2 == 1:
            res.append(a)
    print(len(res))


if __name__ == "__main__":
    main()