from typing import Tuple, Iterable


def main()->None:
    (K, S):Tuple[int, int] = map(int, input().split())

    range_x:Iterable[int] = range(K+1)
    range_y:Iterable[int] = range(K+1)

    counter:int = 0
    for x in range_x:
        for y in range_y:
            z:int = S - x - y
            if 0 <= z <= K:
                counter += 1
    print(counter)





if __name__ == "__main__":
    main()