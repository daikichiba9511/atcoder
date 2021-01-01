from typing import List, Iterable, Set, Dict


def main()->None:
    """
    バケット法を用いた解き方。
    """
    N:int = int(input())
    Q:int = int(input())
    range_N:Iterable[int] = range(N)
    d:List[int] = []
    for i in range_N:
        d[i] = int(input())

    num:Dict[int] = {0} # バケット
    for i in range_N: 
        num[d[i]] +=1 # d[i] が一つ増える
    
    res:int = 0
    range_d:Iterable[int] = range(1,101)
    for i in range_d: # 1<=d<=100なので１から100まで探索
        if num[i]: #0より大きかったら
            res += 1

    print(res)

def main2()->None:
    """
    連想配列を用いてとく。今回はpythonなのでdict or Set
    """
    N:int = int(input())
    d:List[int] = []
    range_N:Iterable[int] = range(N)
    for i in range_N:
        d[i] = int(input())
    
    values:List[int] = []
    for i in ragne_N:
        values[i] = d[i]
    values:Set[int] = set(values) # 重複削除
    
    print(values.size())


if __name__ == "__main__":
    main()
    # main2()