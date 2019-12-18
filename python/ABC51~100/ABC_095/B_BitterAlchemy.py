from typing import List, Iterable

def main()->None:
    N:int, X:int = map(int, input().split())
    range_N:Iterable[int] = range(N)
    m:List[int] = []
    for i in range_N:
        m.append(int(input()))
    
    # 最低でも消費する量を求める。
    min_consump:int = sum(m)
    # 残りのお菓子の元の量
    restL:int = X - min_consump

    # 残りの量と、一つのドーナツを作るのに消費する量で最大公約数を求める
    if rest != 0:
        max_num:int = 0
        for consump in m:
            doughnut:int = rest // consump
            if doughnut > max_num :
                max_num = doughnut
        print(len(m) + max_num)
    else:print(len(m))


if __name__ == "__main__":
    main()