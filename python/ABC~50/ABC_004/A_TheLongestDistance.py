from typing import Iterable, List, Tuple

def main()->None:
    N:int = int(input())
    range_N:Iterable[int] = range(N)
    coodinate:List[int] = []
    for i in range_N:
        (x, y):Tuple[int, int] = map(int, input().split(" "))
        coodinate.append((x, y))

    # ２点間の距離を計算する。　この時最大値を保持すると良さげ
    max_dist:float = 0
    for i in coodinate:
        for j in coodinate:
            dist:float = ((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2) ** (1/2)
            if dist > max_dist:
                max_dist = dist
    print(round(max_dist, 6))





if __name__ == "__main__":
    main()