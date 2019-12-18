from typing import Iterable
# 回答見た


def main()->None:
    N:int = int(input())
    range_N:Iterable[int] = range(1,N+1) # 1<=N<=100
    target:int = 1
    for i in range_N:
        if 2 ** i <= N :
            target = 2 ** i
    print(target)


if __name__ == "__main__":
    main()