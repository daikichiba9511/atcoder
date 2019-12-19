from typing import Iterable, Tuple

def main()->None:
    # 回答を見た
    (A, B):Tuple[int, int] = map(int, input().split())
    range_A2B:Iterable[int] = range(A, B+1)
    count:int = 0
    for i in range_A2B:
        (x, y, g, h, z):Tuple[str, ...] = str(i) # 数字の列を文字列にして分割
        if x == z and y == h: # 回文の条件の３番目を軸に対称性をあるかを判断する。
            count += 1

    print(count)





if __name__ == "__main__":
    main()