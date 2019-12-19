import sys
<<<<<<< HEAD

=======
from typing import List
>>>>>>> master

def main()->None:
    # a_iに１を足すか、１引くか、何もしないかの操作を行って、ある整数個数最大化をする
    # x を決めるとgreedyに決まる。
    # 最後の一つのサンプルがTLEになる。jit の使い方もよくわからん
    # 回答見た。オリジナルは結局最後の一つが通らなかった、O(M^2);M配列の要素の種類の数
<<<<<<< HEAD
    N: int = int(sys.stdin.readline())
    a: List[int] = list(map(int, sys.stdin.readline().split()))
    max_a: int = max(a)
    # print(max_a)
    l: List[int] = [0 for _ in range(max_a+2)] # 配列の初期化、固定長、位置が配列の数字で要素がカウント
    for i in a:
        l[i] += 1
    res: int = 0
    for i in range(0, max_a+1):
        tmp: int = l[i-1]+l[i]+l[i+1]
=======
    N: int = int(sys.stdin.readline())
    a: List[int] = list(map(int, sys.stdin.readline().split()))
    max_a: int = max(a)
    # print(max_a)
    l: List[int] = [0 for _ in range(max_a+2)] # 配列の初期化、固定長、位置が配列の数字で要素がカウント
    for i in a:
        l[i] += 1
    res: int = 0
    for i in range(0, max_a+1):
        tmp: int = l[i-1]+l[i]+l[i+1]
>>>>>>> master
        res = max(res, tmp)
    print(res)


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print(time.time() - start)
