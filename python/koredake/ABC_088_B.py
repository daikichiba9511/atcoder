    from typing import List, Iterable

def main()->None:
    N:int = int(input())
    a:List[int] = [int(input())]

    # 大きい順にソート
    a:List[int] = sort(a, reversed=True)
    
    Alice:int = 0
    Bob:int = 0
    range_N:Iterable[int] = range(N)
    for i in range_N:
        # Alice のターン
        if i % 2 == 0:
            Alice += a[i]
        
        # Bobのターン
        else:
            Bob += a[i]
    
    print(Alice - Bob)