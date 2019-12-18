from typing import Iterable, List

def main()->None:
    N, M = map(int, input().split())
    range_M:Iterable[int] = range(M)
    ab:List[int] = []
    for i in range_M:
        a, b = map(int, input().split())
        ab.append(a)
        ab.append(b)
    range_N:Iterable[int] = range(N)
    for i in range_N:
        print(ab.count(i+1))
    
if __name__ == "__main__":
    main()