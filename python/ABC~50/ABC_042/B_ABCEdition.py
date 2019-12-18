from typing import Iterable, List, Tuple

def main()->None:
    (N, L):Tuple[int, int] = map(int, input().split())
    range_N:Iterable[int] = range(N)
    s:List[int] = []
    for i in range_N:
        s.append(input())
    sorted_s:List[int] = sorted(s)
    print("".join(sorted_s))

if __name__ == "__main__":
    main()