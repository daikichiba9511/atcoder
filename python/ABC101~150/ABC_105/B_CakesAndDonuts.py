from typing import Iterable


def main()->None:
    N:int = int(input())

    range_cakes:Iterable[int] = range((N//4)+1)
    range_donuts:Iterable[int] = range((N//7)+1)

    flag:bool = False
    for i in range_cakes:
        for j in range_donuts:
            if N - 4 * i - 7 * j == 0:
                flag = True
    if flag:
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()