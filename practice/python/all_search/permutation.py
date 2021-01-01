from typing import List, Union
Num = Union[int, float]
Vector = List[Num]

from itertools import permutations

INF : int = 10 ** 8

def main():
    n : int = int(input())
    dist : List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

    # 初期順列
    order : List[int] = [i for i in range(n)]

    # 探索
    res : int = INF

    for i in permutations(order):
        # 順序　order についての所要時間を計算
        tmp_dist : int = 0
        for j in range(n):
            tmp_dist += dist[order[j-1]-1][order[j]-1]

        # 暫定値より小さかったら更新
        if tmp_dist < res:
            res = tmp_dist
    print(res)


if __name__ == "__main__":
    main()
