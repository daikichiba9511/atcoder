from typing import Iterable, List


def main()->None:
    N: int = int(input())
    range_N: Iterable[int] = range(N)
    s: List[int] = []
    for _ in range_N:
        s.append(input())
    M:int = int(input())
    range_M: Iterable[int] = range(M)
    t: List[int] = []
    for _ in range_M:
        t.append(input())
    
    
    max_total: int = 0
    for i in s:
        s_count: int = s.count(i)
        t_count: int = t.count(i)
        total: int  = s_count - t_count
        if total > max_total:
            max_total = total

    print(max_total)


if __name__ == "__main__":
    main()