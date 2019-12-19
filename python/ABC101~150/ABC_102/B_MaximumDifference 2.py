from typing import List


def main()->None:
    N:int = int(input())
    A:List[int] = [i for i in map(int, input().split())]
    diff:int = max(A) - min(A)
    print(diff)

if __name__ == "__main__":
    main()