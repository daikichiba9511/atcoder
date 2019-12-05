from typing import Iterable, Dict, List

DIVIDE:List[str] = ["dream", "dreamer", "erase", "eraser"

def main():->None:
    S:str = input()

    # 後ろからとく代わりに全ての文字列を「左右反転」する
    reversed_S:str = reversed(S)
    range_4:Iterable[int] = range(4)
    for i in range_4:
        reversed_DIVIDE[i] = reversed(DIVIDE[i])

    # 端から切ってく
    can:bool = True
    range_S:Iterable[int] = range(len(S))
    for i in range_S:
        can2:bool = false # 4個の文字列たちどれかで divide　できるか
        range_4:Iterable[int] = range(4)
        for j in range_4:
            d:str = DIVIDE[j]
            if S[i:len(d)] == d: #dでdivideできるか　
                can2 = True
                break
        if !can2: # divide できなかったら
            can = False
            break
    
    if can : print("YES")
    print("NO")

