from typing import Tuple, List

def main()->None:
    (N, K):Tuple[int, int] = map(int, input().split())
    l:List[int] = list(map(int, input().split()))

    sorted_l:List[int] = sorted(l, reverse=True)
    s:int = 0
    for i in sorted_l[:K]:
        s:int += i
    print(s)


if __name__ == "__main__":
    main()